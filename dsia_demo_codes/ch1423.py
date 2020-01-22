import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

def plot_functions(labeled, regressor, d, ax):
  X_arr = np.linspace(labeled["GarageArea"].min(), labeled["GarageArea"].max()).reshape(-1, 1)
  X_arr_poly = PolynomialFeatures(d).fit_transform(X_arr)
  y_arr = regressor.predict(X_arr_poly)
  ax.scatter(labeled["GarageArea"], labeled["SalePrice"], s=5, label="data")
  ax.plot(X_arr, y_arr, c="g", linewidth=2, label="h")
  ax.set_ylim(labeled["SalePrice"].min(), labeled["SalePrice"].max())
  ax.legend(loc="upper left")
  
def plot_coefficients(regressor, ax, alpha):
  coef = regressor.coef_.ravel()
  ax.semilogy(np.abs(coef), marker='^', label="alpha = {:.1E}".format(alpha))
  ax.set_ylim((1e-10, 1e2))
  ax.axhline(y=1, ls="--", color="r")
  ax.legend(loc='upper right')
  
labeled = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv")
X = labeled.loc[:, "GarageArea"].values.reshape(-1, 1)
y = labeled.loc[:, "SalePrice"].values.reshape(-1, 1)
degree = 10
X_poly = PolynomialFeatures(degree).fit_transform(X)
X_train, X_validation, y_train, y_validation = train_test_split(X_poly, y, test_size=0.3, random_state=123)
# 正規化係數 alpha
alphas = [0, 1e3, 1e6, 1e9, 1e12]
# Visualization
fig, axes = plt.subplots(5, 2, figsize=(12, 16))
for i, alpha in enumerate(alphas):
  ridge = Ridge(alpha=alpha)
  ridge.fit(X_train, y_train)
  ax = axes[i, 0]
  plot_functions(labeled, ridge, d=degree, ax=ax)
  ax = axes[i, 1]
  plot_coefficients(ridge, ax=ax, alpha=alpha)
plt.show()