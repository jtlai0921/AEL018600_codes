import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

def compute_cost(X, y, thetas):
  m = X.shape[0]
  y_hat = np.dot(X, thetas)
  J = 1/(2*m)*np.sum(np.square(y_hat - y))
  return J

def gradient_descent(X, y, alpha=0.01, num_iters=1500):
  m = X.shape[0]
  J_history = np.zeros(num_iters)
  thetas = np.array([0, 0], dtype=float).reshape(-1, 1)
  for num_iter in range(num_iters):
    y_hat = np.dot(X, thetas)
    loss = y_hat - y
    gradient = np.dot(X.T, loss)
    thetas -= alpha*gradient/m
    J_history[num_iter] = compute_cost(X, y, thetas)
  return thetas, J_history

def standard_scaler(x):
  mean_x = x.mean()
  std_x = x.std()
  standard_x = (x - mean_x)/std_x
  return standard_x

labeled = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv")
train, validation = train_test_split(labeled, test_size=0.3, random_state=123)
X_train = train.loc[:, "GrLivArea"].values.reshape(-1, 1)
y_train = train.loc[:, "SalePrice"].values.reshape(-1, 1)
reg = LinearRegression()
reg.fit(X_train, y_train)
print("Thetas from Scikit-Learn:")
print(reg.intercept_)
print(reg.coef_)
# Standardization
X_train_ss = standard_scaler(X_train)
y_train_ss = standard_scaler(y_train)
ones = np.ones(X_train.shape[0], dtype=int).reshape(-1, 1)
X_train_ss = np.concatenate([ones, X_train_ss], axis=1)
thetas, J_history = gradient_descent(X_train_ss, y_train_ss, alpha=0.001, num_iters=5000)
print("Standardized thetas from manual gradient descent:")
print(thetas)
# Rescaling
theta_0_pron = thetas[0, 0]
theta_1_pron = thetas[1, 0]
mu_y = y_train.mean()
sigma_y = y_train.std()
mu_X = X_train.mean()
sigma_X = X_train.std()
theta_0 = mu_y + sigma_y*theta_0_pron - sigma_y*mu_X*theta_1_pron/sigma_X
theta_1 = sigma_y*theta_1_pron/sigma_X
print("Rescaled thetas from manual gradient descent:")
print(theta_0)
print(theta_1)