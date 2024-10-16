#Random Forest
from sklearn.ensemble import RandomForestClassifier

# Initialize the model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

# Predict the test set results
y_pred_rf = rf_model.predict(X_test)

# Evaluate the model
print("Random Forest Accuracy:", accuracy_score(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf))

'''
RandomForestClassifier: Creates a random forest model with 100 trees (n_estimators=100).
.fit(): Trains the model using the training data.
.predict(): Predicts the target variable (vegetation type) for the test set.
accuracy_score and classification_report: Used to evaluate model performance.'''


######Grid Search for Random Forest######
#Grid Search for Random Forest
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# Define the parameter grid for Random Forest
param_grid_rf = {
    'n_estimators': [50, 100, 200],  # Number of trees
    'max_depth': [None, 10, 20, 30],  # Maximum depth of each tree
    'min_samples_split': [2, 5, 10],  # Minimum number of samples required to split a node
    'min_samples_leaf': [1, 2, 4]  # Minimum number of samples required in a leaf node
}

# Initialize the Random Forest model
rf_model = RandomForestClassifier(random_state=42)

# Initialize GridSearchCV
grid_search_rf = GridSearchCV(estimator=rf_model, param_grid=param_grid_rf,
                              cv=3, n_jobs=-1, verbose=2)

# Perform grid search
grid_search_rf.fit(X_train, y_train)

# Best parameters and score
print("Best Parameters for Random Forest:", grid_search_rf.best_params_)
print("Best Random Forest Score:", grid_search_rf.best_score_)



######Randomized Search for Random Forest#####
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import randint

# Define the parameter distribution for Random Forest
param_dist_rf = {
    'n_estimators': randint(50, 300),  # Random integer values between 50 and 300 for the number of trees
    'max_depth': [None, 10, 20, 30, 40, 50],  # Maximum depth of the trees
    'min_samples_split': randint(2, 10),  # Random integer values for minimum number of samples to split
    'min_samples_leaf': randint(1, 5),  # Random integer values for minimum samples in a leaf
    'bootstrap': [True, False]  # Whether bootstrap samples are used when building trees
}

# Initialize Random Forest model
rf_model = RandomForestClassifier(random_state=42)

# Initialize RandomizedSearchCV
random_search_rf = RandomizedSearchCV(estimator=rf_model, param_distributions=param_dist_rf,
                                      n_iter=50, cv=3, random_state=42, n_jobs=-1, verbose=2)

# Perform random search
random_search_rf.fit(X_train, y_train)
# Best parameters and score
print("Best Parameters for Random Forest:", random_search_rf.best_params_)
print("Best Random Forest Score:", random_search_rf.best_score_)








'//////////////2////////////'

#XGBoost
import xgboost as xgb

# Initialize the model
xgb_model = xgb.XGBClassifier(n_estimators=100, use_label_encoder=False, eval_metric='mlogloss')

# Train the model
xgb_model.fit(X_train, y_train)

# Predict the test set results
y_pred_xgb = xgb_model.predict(X_test)

# Evaluate the model
print("XGBoost Accuracy:", accuracy_score(y_test, y_pred_xgb))
print(classification_report(y_test, y_pred_xgb))

"""XGBClassifier: Creates an XGBoost classifier with 100 trees.
eval_metric='mlogloss': Metric for evaluating the model, multi-class log loss in this case.
use_label_encoder=False: Disables XGBoost's internal label encoder.
.fit(), .predict(), accuracy_score, and classification_report: Same as explained in the Random Forest model."""




#####Grid Search for XGBoost#####
import xgboost as xgb

# Define the parameter grid for XGBoost
param_grid_xgb = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 6, 10],
    'learning_rate': [0.01, 0.1, 0.3],
    'subsample': [0.6, 0.8, 1.0],
    'colsample_bytree': [0.6, 0.8, 1.0]
}

# Initialize the XGBoost model
xgb_model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')

# Initialize GridSearchCV
grid_search_xgb = GridSearchCV(estimator=xgb_model, param_grid=param_grid_xgb,
                               cv=3, n_jobs=-1, verbose=2)

# Perform grid search
grid_search_xgb.fit(X_train, y_train)

# Best parameters and score
print("Best Parameters for XGBoost:", grid_search_xgb.best_params_)
print("Best XGBoost Score:", grid_search_xgb.best_score_)




#####Randomized Search for XGBoost#####
import xgboost as xgb
from scipy.stats import uniform

# Define the parameter distribution for XGBoost
param_dist_xgb = {
    'n_estimators': randint(50, 200),  # Random integer values between 50 and 200 for number of trees
    'max_depth': randint(3, 10),  # Random depth between 3 and 10
    'learning_rate': uniform(0.01, 0.3),  # Random float between 0.01 and 0.3
    'subsample': uniform(0.6, 0.4),  # Random float between 0.6 and 1.0
    'colsample_bytree': uniform(0.6, 0.4)  # Random float between 0.6 and 1.0
}

# Initialize the XGBoost model
xgb_model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')

# Initialize RandomizedSearchCV
random_search_xgb = RandomizedSearchCV(estimator=xgb_model, param_distributions=param_dist_xgb,
                                       n_iter=50, cv=3, random_state=42, n_jobs=-1, verbose=2)

# Perform random search
random_search_xgb.fit(X_train, y_train)

# Best parameters and score
print("Best Parameters for XGBoost:", random_search_xgb.best_params_)
print("Best XGBoost Score:", random_search_xgb.best_score_)





'////////////////3/////////////////////////'
#Support Vector Machine (SVM)
from sklearn.svm import SVC

# Initialize the model
svm_model = SVC(kernel='rbf', random_state=42)

# Train the model
svm_model.fit(X_train_scaled, y_train)

# Predict the test set results
y_pred_svm = svm_model.predict(X_test_scaled)

# Evaluate the model
print("SVM Accuracy:", accuracy_score(y_test, y_pred_svm))
print(classification_report(y_test, y_pred_svm))

"""
SVC: Creates an SVM classifier using the Radial Basis Function (RBF) kernel.
.fit(), .predict(): Same as the other models.
We use the scaled training and test sets (X_train_scaled, X_test_scaled) because SVM requires the data to be scaled."""



#####Grid Search for SVM#####
from sklearn.svm import SVC

# Define the parameter grid for SVM
param_grid_svm = {
    'C': [0.1, 1, 10],  # Regularization parameter
    'gamma': ['scale', 'auto'],  # Kernel coefficient for RBF
    'kernel': ['rbf']  # Type of kernel
}

# Initialize the SVM model
svm_model = SVC()

# Initialize GridSearchCV
grid_search_svm = GridSearchCV(estimator=svm_model, param_grid=param_grid_svm,
                               cv=3, n_jobs=-1, verbose=2)

# Perform grid search
grid_search_svm.fit(X_train_scaled, y_train)

# Best parameters and score
print("Best Parameters for SVM:", grid_search_svm.best_params_)
print("Best SVM Score:", grid_search_svm.best_score_)


#####Randomized Search for SVM#####

from sklearn.svm import SVC
from scipy.stats import uniform

# Define the parameter distribution for SVM
param_dist_svm = {
    'C': uniform(0.1, 10),  # Random float values between 0.1 and 10 for regularization parameter
    'gamma': ['scale', 'auto'],  # Kernel coefficient options
    'kernel': ['rbf']  # Fixed kernel type (Radial Basis Function)
}

# Initialize the SVM model
svm_model = SVC()

# Initialize RandomizedSearchCV
random_search_svm = RandomizedSearchCV(estimator=svm_model, param_distributions=param_dist_svm,
                                       n_iter=50, cv=3, random_state=42, n_jobs=-1, verbose=2)

# Perform random search
random_search_svm.fit(X_train_scaled, y_train)

# Best parameters and score
print("Best Parameters for SVM:", random_search_svm.best_params_)
print("Best SVM Score:", random_search_svm.best_score_)
