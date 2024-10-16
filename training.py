from sklearn.model_selection import train_test_split, cross_validate
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Split the Dataset into train set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3,
                                                    random_state = 42)

model = RandomForestClassifier(n_estimators = 100, max_depth = 10, max_features = 'sqrt', n_jobs = -1)

scoring = ['accuracy', 'recall', 'precision', 'f1_score']

cv_results = cross_validate(model,
                            X_train,
                            y_train,
                            scoring = scoring,
                            cv = 5)

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
