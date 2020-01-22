import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def sigmoid(z):
  return 1/(1 + np.exp(-z))

def step(g_y_hat, threshold=0.5):
  return np.where(g_y_hat >= threshold, 1, 0).reshape(-1, 1)

labeled = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/Titanic-Machine-Learning-from-Disaster/train.csv")
# Removed observations without Age
labeled = labeled[~labeled["Age"].isna()]
survived = labeled[labeled["Survived"] == 1]
dead = labeled[labeled["Survived"] == 0]
train, validation = train_test_split(labeled, test_size=0.3, random_state=123)
X_train = train.loc[:, ["Fare", "Age"]].values
y_train = train.loc[:, "Survived"].values
logistic_clf = LogisticRegression()
logistic_clf.fit(X_train, y_train)
fit_intercept = logistic_clf.intercept_.reshape(-1, 1)
fit_coef = logistic_clf.coef_.reshape(-1, 1)
thetas = np.concatenate([fit_intercept, fit_coef])
# Decision boundary plot
fare_min, fare_max = labeled["Fare"].min(), labeled["Fare"].max()
age_min, age_max = labeled["Age"].min(), labeled["Age"].max()
fare_arr = np.linspace(fare_min - 5, fare_max + 5, 1000)
age_arr = np.linspace(age_min - 5, age_max + 5, 1000)
xx, yy = np.meshgrid(fare_arr, age_arr)
ones = np.ones(xx.size).reshape(-1, 1)
X_grid = np.concatenate([ones, xx.reshape(-1, 1), yy.reshape(-1, 1)], axis=1)
y_grid = np.dot(X_grid, thetas)
g_y_grid = sigmoid(y_grid)
y_grid_pred = step(g_y_grid)
Z = y_grid_pred.reshape(xx.shape)
plt.scatter(survived["Fare"], survived["Age"], label="Survived", marker="o", color="blue")
plt.scatter(dead["Fare"], dead["Age"], label="Dead", marker="x", color="red")
plt.contourf(xx, yy, Z, alpha=0.4, cmap=plt.cm.coolwarm_r)
plt.legend(loc="upper right")
plt.xlabel("Fare")
plt.ylabel("Age")
plt.show()