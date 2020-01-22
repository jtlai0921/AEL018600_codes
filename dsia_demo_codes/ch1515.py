import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def sigmoid(z):
  return 1/(1 + np.exp(-z))

def step(g_y_hat, threshold=0.5):
  return np.where(g_y_hat >= threshold, 1, 0).reshape(-1, 1)

labeled = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/Titanic-Machine-Learning-from-Disaster/train.csv")
# Removed observations without Age
labeled = labeled[~labeled["Age"].isna()]
train, validation = train_test_split(labeled, test_size=0.3, random_state=123)
X_train = train.loc[:, ["Age", "Fare"]].values
y_train = train.loc[:, "Survived"].values
logistic_clf = LogisticRegression()
logistic_clf.fit(X_train, y_train)
fit_intercept = logistic_clf.intercept_.reshape(-1, 1)
fit_coef = logistic_clf.coef_.reshape(-1, 1)
thetas = np.concatenate([fit_intercept, fit_coef])
X_validation = validation.loc[:, ["Age", "Fare"]].values
ones = np.ones(X_validation.shape[0]).reshape(-1, 1)
X_validation = np.concatenate([ones, X_validation], axis=1)
y_hat = np.dot(X_validation, thetas)
g_y_hat = sigmoid(y_hat)
y_pred = step(g_y_hat)
y_true = validation.loc[:, "Survived"].values.reshape(-1, 1)
print("Thetas from sklearn:")
print(thetas)
print("Before Sigmoid transform:")
print(y_hat[:5])
print("After Sigmoid transform:")
print(g_y_hat[:5])
print("After Step transform:")
print(y_pred[:5])
print("True condition:")
print(y_true[:5])