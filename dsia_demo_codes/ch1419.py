import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def get_best_degree(X_train, y_train, X_validation, y_validation, d=10):
  degrees = range(1, d+1)
  mse_train_arr = np.zeros(d)
  mse_validation_arr = np.zeros(d)
  for degree in degrees:
    X_train_poly = PolynomialFeatures(degree).fit_transform(X_train)
    X_validation_poly = PolynomialFeatures(degree).fit_transform(X_validation)
    reg = LinearRegression()
    reg.fit(X_train_poly, y_train)
    y_hat = reg.predict(X_train_poly)
    mse_train = mean_squared_error(y_train, y_hat)
    y_hat = reg.predict(X_validation_poly)
    mse_validation = mean_squared_error(y_validation, y_hat)
    mse_train_arr[degree - 1] = mse_train
    mse_validation_arr[degree - 1] = mse_validation
  best_degree = mse_validation_arr.argmin() + 1
  return mse_train_arr, mse_validation_arr, best_degree

def get_bd_history(labeled, num_iters=100):
  bd_history = np.zeros(num_iters)
  for num_iter in range(num_iters):
    train, validation = train_test_split(labeled, test_size=0.3)
    X_train = train.loc[:, "YearBuilt"].values.reshape(-1, 1)
    X_validation = validation.loc[:, "YearBuilt"].values.reshape(-1, 1)
    y_train = train.loc[:, "SalePrice"].values.reshape(-1, 1)
    y_validation = validation.loc[:, "SalePrice"].values.reshape(-1, 1)
    best_degree = get_best_degree(X_train, y_train, X_validation, y_validation)[2]
    bd_history[num_iter] = best_degree
  df = pd.DataFrame()
  df["bd_history"] = bd_history
  grouped = df.groupby("bd_history")
  return grouped.size().sort_values(ascending=False)

labeled = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv")
get_bd_history(labeled)