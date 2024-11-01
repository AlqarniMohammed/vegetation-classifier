import pandas as pd
from sklearn.model_selection import train_test_split
from vegatation.params import *
from vegatation.ml_logic.data import *
from vegatation.ml_logic.preprocessor import *
from vegatation.ml_logic.model import *

data = load_data(DATASET)
print("data loaded")
unencoded_data = unEncoded_data(data)
print("encode data")
unencoded_data = compress(unencoded_data)
print("unencoded data")
unencoded_data = clean_data(unencoded_data)
print("clean data")
# Split into features (X) and target (y)
X = unencoded_data.drop('cover_type', axis=1)  # Drop the target column 'Cover_Type'
y = unencoded_data['cover_type']

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2,
                                                    random_state = 42)
print("xtrain and xtest done")
pipeline, X_train_processed, X_test_processed, y_train_processed, y_test_processed = processed_data(X_train, X_test,y_train, y_test)

model = trained_model(X_train_processed, y_train_processed)
print("model trained")
y_pred = prediction(model, X_test_processed, y_test_processed)
print(f"y_pred: {y_pred}")
