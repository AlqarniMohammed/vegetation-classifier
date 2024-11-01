import pandas as pd
# $WIPE_BEGIN

from vegatation.ml_logic.model import load_model
from vegatation.ml_logic.preprocessor import load_pipeline
# $WIPE_END

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# $WIPE_BEGIN
# 💡 Preload the model to accelerate the predictions
# We want to avoid loading the heavy Deep Learning model from MLflow at each `get("/predict")`
# The trick is to load the model in memory when the Uvicorn server starts
# and then store the model in an `app.state.model` global variable, accessible across all routes!
# This will prove very useful for the Demo Day
app.state.model = load_model()
# $WIPE_END

# http://127.0.0.1:8000/predict?pickup_datetime=2014-07-06+19:18:00&pickup_longitude=-73.950655&pickup_latitude=40.783282&dropoff_longitude=-73.984365&dropoff_latitude=40.769802&passenger_count=2
@app.get("/predict")
def predict(
        Elevation: float,  # 2014-07-06 19:18:00
        Aspect: float,    # -73.950655
        Slope: float,     # 40.783282
        Horizontal_Distance_To_Hydrology: float,
        Vertical_Distance_To_Hydrology: float,# -73.984365
        Horizontal_Distance_To_Roadways: float,    # 40.769802
        Hillshade_9am: float,
        Hillshade_Noon: float,
        Hillshade_3pm: float,
        Horizontal_Distance_To_Fire_Points: float,
        wilderness: str,
        Soil_Type: str,
    ):
    """
    Make a single course prediction.
    Assumes `pickup_datetime` is provided as a string by the user in "%Y-%m-%d %H:%M:%S" format
    Assumes `pickup_datetime` implicitly refers to the "US/Eastern" timezone (as any user in New York City would naturally write)
    """
    # $CHA_BEGIN

    # 💡 Optional trick instead of writing each column name manually:
    # locals() gets us all of our arguments back as a dictionary
    # https://docs.python.org/3/library/functions.html#locals
    X_pred = pd.DataFrame({
       'Elevation': [Elevation],
        'Aspect': [Aspect],
        'Slope': [Slope],
        'Horizontal_Distance_To_Hydrology': [ Horizontal_Distance_To_Hydrology],
        'Vertical_Distance_To_Hydrology': [Vertical_Distance_To_Hydrology],
        'Horizontal_Distance_To_Roadways': [Horizontal_Distance_To_Roadways],
        'Hillshade_9am':[Hillshade_9am],
        'Hillshade_Noon':[Hillshade_Noon],
        'Hillshade_3pm':[Hillshade_3pm],
        'Horizontal_Distance_To_Fire_Points':[Horizontal_Distance_To_Fire_Points],
        'wilderness':[wilderness],
        'Soil_Type':[Soil_Type],
    })


    model = app.state.model
    assert model is not None

    app.state.pipeline = load_pipeline()
    pipeline = app.state.pipeline

    X_processed = pipeline.transform(X_pred)
    y_pred = model.predict(X_processed)

    label_dict = {
    0: "Spruce/Fir",
    1: "Lodgepole Pine",
    2: "Ponderosa Pine",
    3: "Cottonwood/Willow",
    4: "Aspen",
    5: "Douglas-fir",
    6: "Krummholz"
    }

    y_pred1 = [label_dict[i] for i in y_pred]

    # ⚠️ fastapi only accepts simple Python data types as a return value
    # among them dict, list, str, int, float, bool
    # in order to be able to convert the api response to JSON
    #return 'Hello'
    return y_pred1[0]


@app.get("/")
def root():
    # $CHA_BEGIN
    return dict(greeting="Hello")
    # $CHA_END
