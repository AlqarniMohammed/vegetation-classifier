import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn import set_config
import pickle

def numeric_preprocessor(X_train, X_test):

    num_preprocessor = ColumnTransformer([
    ('standard_transformer', StandardScaler(), ['Elevation', 'Slope']),
    ('minmax_transformer', MinMaxScaler(), ['Aspect', 'Hillshade_9am', 'Hillshade_Noon', 'Hillshade_3pm']),
    ('robust_transformer', RobustScaler(), ['Horizontal_Distance_To_Hydrology', 'Vertical_Distance_To_Hydrology',
                                        'Horizontal_Distance_To_Roadways', 'Horizontal_Distance_To_Fire_Points'])]
    )

    X_train = num_preprocessor.fit_transform(X_train)
    X_test = num_preprocessor.transform(X_test)

    X_train_df = pd.DataFrame(X_train, columns=num_preprocessor.get_feature_names_out())
    X_test_df = pd.DataFrame(X_test, columns=num_preprocessor.get_feature_names_out())

    return X_train_df, X_test_df

def wilderness_preprocessor(X_train, X_test):

    oh_encoder = OneHotEncoder(drop='if_binary', sparse_output=False, handle_unknown='ignore')

    wilderness_encoded_train = oh_encoder.fit_transform(X_train[['wilderness']])
    wilderness_encoded_test = oh_encoder.transform(X_test[['wilderness']])

    wilderness_train_df = pd.DataFrame(
    wilderness_encoded_train,
    columns=oh_encoder.get_feature_names_out()
    )

    wilderness_test_df = pd.DataFrame(
    wilderness_encoded_test,
    columns=oh_encoder.get_feature_names_out()
    )

    return wilderness_train_df, wilderness_test_df

def soil_preprocessor(X_train, X_test):

    oh_encoder = OneHotEncoder(drop='if_binary', sparse_output=False, handle_unknown='ignore')

    soil_encoded_train = oh_encoder.fit_transform(X_train[['Soil_Type']])
    soil_encoded_test = oh_encoder.transform(X_test[['Soil_Type']])

    soil_train_df = pd.DataFrame(
    soil_encoded_train,
    columns=oh_encoder.get_feature_names_out()
    )

    soil_test_df = pd.DataFrame(
    soil_encoded_test,
    columns=oh_encoder.get_feature_names_out()
    )

    return soil_train_df, soil_test_df

def preprocessed_target(y_train, y_test):

    label_encoder = LabelEncoder()

    y_train_processed = label_encoder.fit_transform(y_train)
    y_test_processed = label_encoder.transform(y_test)

    return y_train_processed, y_test_processed


def processed_features(X_train, X_test, X_train_df, X_test_df, wilderness_train_df, wilderness_test_df, soil_train_df, soil_test_df):

    X_train = X_train.drop(columns=['wilderness', 'Soil_Type']).reset_index(drop=True)
    X_test = X_test.drop(columns=['wilderness', 'Soil_Type']).reset_index(drop=True)

    X_train_processed = pd.concat([X_train_df, wilderness_train_df, soil_train_df], axis=1)
    X_test_processed = pd.concat([X_test_df, wilderness_test_df, soil_test_df], axis=1)

    return X_train_processed, X_test_processed

def processed_data(X_train, X_test,y_train, y_test):

    pipeline = ColumnTransformer([
    ('std_transformer', StandardScaler(), ['Elevation', 'Slope']),
    ('minmax_transformer', MinMaxScaler(), ['Aspect', 'Hillshade_9am', 'Hillshade_Noon', 'Hillshade_3pm']),
    ('rb_transformer', RobustScaler(), ['Horizontal_Distance_To_Hydrology', 'Vertical_Distance_To_Hydrology',
                                  'Horizontal_Distance_To_Roadways', 'Horizontal_Distance_To_Fire_Points']),
    ('wilderness_transformer', OneHotEncoder(drop='if_binary', sparse_output=False, handle_unknown='ignore'), ['wilderness']),
    ('Soil_Type_transformer', OneHotEncoder(drop='if_binary', sparse_output=False, handle_unknown='ignore'), ['Soil_Type'])]
    )

    label_encoder = LabelEncoder()

    y_train_processed = label_encoder.fit_transform(y_train)
    y_test_processed = label_encoder.transform(y_test)

    X_train_processed = pipeline.fit_transform(X_train)
    X_test_processed = pipeline.transform(X_test)

    set_config(display='diagram')

    return pipeline, X_train_processed, X_test_processed, y_train_processed, y_test_processed


def load_pipeline():

    pipeline = pickle.load(open("/home/mohammedalqarni/code/AlqarniMohammed/vegetation-classifier/vegatation/ml_logic/pipeline2.pkl","rb"))

    return pipeline
