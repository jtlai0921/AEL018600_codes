import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

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

labeled = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv")
train, validation = train_test_split(labeled, test_size=0.3, random_state=123)
X_train = train.loc[:, "GrLivArea"].values.reshape(-1, 1)
y_train = train.loc[:, "SalePrice"].values.reshape(-1, 1)
reg = LinearRegression()
reg.fit(X_train, y_train)
print("Thetas from Scikit-Learn:")
print(reg.intercept_)
print(reg.coef_)
ones = np.ones(X_train.shape[0], dtype=int).reshape(-1, 1)
X_train = np.concatenate([ones, X_train], axis=1)
thetas, J_history = gradient_descent(X_train, y_train, alpha=0.0000000001, num_iters=20000)
print("Thetas from manual gradient descent:")
print(thetas)
plt.plot(J_history)
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.show()