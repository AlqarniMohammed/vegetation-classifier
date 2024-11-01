from sklearn.ensemble import RandomForestClassifier
import pickle
from vegatation.ml_logic.preprocessor import *
from sklearn.metrics import accuracy_score, precision_score, recall_score
import requests
import os

def save_model(model):

    with open("vegatation.pkl", "wb") as file:
        pickle.dump(model, file)

def trained_model(X_train_processed, y_train_processed):

    model = RandomForestClassifier(n_estimators = 200,
                                   max_depth = 30,
                                   n_jobs = -1,
                                   min_samples_leaf = 1,
                                   min_samples_split = 2)

    model.fit(X_train_processed, y_train_processed)
    save_model(model)
    return model

def prediction(model, X_test_processed, y_test_processed):

    y_pred = model.predict(X_test_processed)

    accuracy = accuracy_score(y_test_processed, y_pred)
    precision = precision_score(y_test_processed, y_pred, average='macro')
    recall = recall_score(y_test_processed, y_pred, average='macro')

    print(f'Accuracy: {accuracy}')
    print(f'Precision: {precision}')
    print(f'Recall: {recall}')

    label_dict = {
    0: "Spruce/Fir",
    1: "Lodgepole Pine",
    2: "Ponderosa Pine",
    3: "Cottonwood/Willow",
    4: "Aspen",
    5: "Douglas-fir",
    6: "Krummholz"
    }

    y_pred = [label_dict[i] for i in y_pred]

    return y_pred

def load_model():

    path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    final_path = os.path.join(path, 'models', 'vegatation.pkl')
    print(final_path)
    model = pickle.load(open(final_path,"rb"))

    return model


#   model = pickle.load(open("vegatation.pkl","rb"))
