from sklearn.model_selection import train_test_split, cross_validate
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Split the Dataset into train set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3,
                                                    random_state = 42)



param_grid_rf = {
    'n_estimators': [50, 100, 200],  # Number of trees
    'max_depth': [None, 10, 20, 30],  # Maximum depth of each tree
    'min_samples_split': [2, 5, 10],  # Minimum number of samples required to split a node
    'min_samples_leaf': [1, 2, 4]  # Minimum number of samples required in a leaf node
}
rf_model = RandomForestClassifier(random_state=42)

grid_search_rf = GridSearchCV(estimator=rf_model, param_grid=param_grid_rf,
                              cv=3, n_jobs=-1)

grid_search_rf.fit(X_train, y_train)

# Best parameters and score
print("Best Parameters for Random Forest:", grid_search_rf.best_params_)
print("Best Random Forest Score:", grid_search_rf.best_score_)



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
                                      cv=3, random_state=42, n_jobs=-1)

# Perform random search
random_search_rf.fit(X_train, y_train)
# Best parameters and score
print("Best Parameters for Random Forest:", random_search_rf.best_params_)
print("Best Random Forest Score:", random_search_rf.best_score_)



model = RandomForestClassifier(n_estimators = 100, max_depth = 10, max_features = 'sqrt', n_jobs = -1)

scoring = ['accuracy', 'recall', 'precision', 'f1_score']

cv_results = cross_validate(model,
                            X_train,
                            y_train,
                            scoring = scoring,
                            cv = 10)

print(f"Accuracy: {cv_results['test_accuracy']}")
print(f"Recall: {cv_results['test_recall']}")
print(f"Precision: {cv_results['test_precision']}")
print(f"F1 Score: {cv_results['test_f1']}")

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')
