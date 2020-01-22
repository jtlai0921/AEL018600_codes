import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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

labeled = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv")
train, validation = train_test_split(labeled, test_size=0.3, random_state=123)
X_train = train.loc[:, "YearBuilt"].values.reshape(-1, 1)
X_validation = validation.loc[:, "YearBuilt"].values.reshape(-1, 1)
y_train = train.loc[:, "SalePrice"].values.reshape(-1, 1)
y_validation = validation.loc[:, "SalePrice"].values.reshape(-1, 1)
d = 10
mse_train_arr, mse_validation_arr, best_degree = get_best_degree(X_train, y_train, X_validation, y_validation, d=10)
print("Best degree: {}".format(best_degree))
degrees = range(1, d+1)
plt.plot(degrees, mse_train_arr, c="red", marker="s", label="Train")
plt.plot(degrees, mse_validation_arr, c="g", marker="^", label="Validation")
plt.xticks(degrees)
plt.axvline(best_degree, label="Best Degree: {}".format(best_degree))
plt.legend(loc="upper right")
plt.xlabel("Degree")
plt.ylabel("MSE")
plt.show()