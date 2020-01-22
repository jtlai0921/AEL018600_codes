import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from scipy.optimize import minimize

def sigmoid(z):
  return 1/(1 + np.exp(-z))

# Must put thetas as the first arg
def cost_function(thetas, X, y):
  m = X.shape[0]
  h = sigmoid(X.dot(thetas))
  J = -1*(1/m)*(np.log(h).T.dot(y)+np.log(1-h).T.dot(1-y))
  # log(0) approached -Inf results in NaN
  if np.isnan(J[0]):
    return(np.inf)
  else:
    return(J[0])

# Must put thetas as the first arg
def gradient(thetas, X, y):
  m = y.size
  h = sigmoid(X.dot(thetas.reshape(-1,1)))
  grad =(1/m)*X.T.dot(h-y)
  return(grad.ravel())

def step(g_y_hat, threshold=0.5):
  return np.where(g_y_hat >= threshold, 1, 0).reshape(-1, 1)

labeled = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/Titanic-Machine-Learning-from-Disaster/train.csv")
# Removed observations without Age
labeled = labeled[~labeled["Age"].isna()]
train, validation = train_test_split(labeled, test_size=0.3, random_state=123)
X_train = train.loc[:, ["Age", "Fare"]].values
ones = np.ones(X_train.shape[0]).reshape(-1, 1)
X_train = np.concatenate([ones, X_train], axis=1)
y_train = train.loc[:, "Survived"].values.reshape(-1, 1)
initial_thetas = np.zeros(X_train.shape[1])
res = minimize(cost_function, initial_thetas, args=(X_train, y_train), method=None, jac=gradient, options={'maxiter':400})
thetas = res.x.reshape(-1, 1)
X_validation = validation.loc[:, ["Age", "Fare"]].values
ones = np.ones(X_validation.shape[0]).reshape(-1, 1)
X_validation = np.concatenate([ones, X_validation], axis=1)
y_hat = np.dot(X_validation, thetas)
print("Before Sigmoid transform:")
print(y_hat[:5])
g_y_hat = sigmoid(y_hat)
print("After Sigmoid transform:")
print(g_y_hat[:5])
y_pred = step(g_y_hat)
print("After Step transform:")
print(y_pred[:5])