import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def get_mse(X_arr, y_arr, thetas):
  m = X_arr.size
  theta_0 = thetas[0, 0]
  theta_1 = thetas[1, 0]
  y_hat = theta_0 + theta_1*X_arr
  err = y_hat - y_arr
  se = np.sum(err**2)
  return se/m

def get_mse_vectorized(X, y, thetas):
  m = X.shape[0]
  y_hat = np.dot(X, thetas)
  err = y_hat - y
  se = np.dot(err.T, err)
  return se[0, 0]/m

labeled = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv")
train, validation = train_test_split(labeled, test_size=0.3, random_state=123)
X_train = train.loc[:, "GrLivArea"].values.reshape(-1, 1)
y_train = train.loc[:, "SalePrice"].values.reshape(-1, 1)
X_validation = validation.loc[:, "GrLivArea"].values.reshape(-1, 1)
ones = np.ones(X_validation.shape[0]).reshape(-1, 1)
X_validation = np.concatenate([ones, X_validation], axis=1)
y_validation = validation.loc[:, "SalePrice"].values.reshape(-1, 1)
reg = LinearRegression()
reg.fit(X_train, y_train)
theta_0 = reg.intercept_[0]
theta_1 = reg.coef_[0, 0]
thetas = np.array([theta_0, theta_1]).reshape(-1, 1)
mse = get_mse(validation.loc[:, "GrLivArea"].values, validation.loc[:, "SalePrice"].values, thetas)
vectorized_mse = get_mse_vectorized(X_validation, y_validation, thetas)
print("MSE: {:.0f}".format(mse))
print("MSE(vectorized): {:.0f}".format(vectorized_mse))