import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

def get_best_degree(X_labeled, y_labeled, k=5, d=10):
  kf = KFold(n_splits=k, shuffle=True)
  degrees = range(1, d+1)
  mse_train_avg_arr = np.zeros(d)
  mse_validation_avg_arr = np.zeros(d)
  for degree in degrees:
    mse_train_arr = []
    mse_validation_arr = []
    for train_idx, valid_idx in kf.split(X_labeled):
      X_train, X_validation = X_labeled[train_idx], X_labeled[valid_idx]
      y_train, y_validation = y_labeled[train_idx], y_labeled[valid_idx]
      X_train_poly = PolynomialFeatures(d).fit_transform(X_train)
      X_validation_poly =  PolynomialFeatures(d).fit_transform(X_validation)
      reg = LinearRegression()
      reg.fit(X_train_poly, y_train)
      y_hat = reg.predict(X_train_poly)
      mse_train = mean_squared_error(y_train, y_hat)
      y_hat = reg.predict(X_validation_poly)
      mse_validation = mean_squared_error(y_validation, y_hat)
      mse_train_arr.append(mse_train)
      mse_validation_arr.append(mse_validation)
    mse_train_avg_arr[degree - 1] = np.array(mse_train_arr).mean()
    mse_validation_avg_arr[degree - 1] = np.array(mse_validation_arr).mean()
  best_degree = mse_validation_avg_arr.argmin() + 1
  return mse_train_avg_arr, mse_validation_avg_arr, best_degree

labeled = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv")
X_labeled = labeled.loc[:, "YearBuilt"].values.reshape(-1, 1)
y_labeled = labeled.loc[:, "SalePrice"].values.reshape(-1, 1)
mse_train_avg_arr, mse_validation_avg_arr, best_degree = get_best_degree(X_labeled, y_labeled)
print("Best degree: {}".format(best_degree))
d = 10
degrees = range(1, d+1)
plt.plot(degrees, mse_train_avg_arr, c="r", marker="s", label="Train")
plt.plot(degrees, mse_validation_avg_arr, c="g", marker="^", label="Validation")
plt.xticks(degrees)
plt.axvline(best_degree, label="Best Degree: {}".format(best_degree))
plt.legend(loc="upper left")
plt.xlabel("Degree")
plt.ylabel("MSE")
plt.show()