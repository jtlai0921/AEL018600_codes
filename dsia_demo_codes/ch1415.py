import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

labeled = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv")
train, validation = train_test_split(labeled, test_size=0.3, random_state=123)
X_train = train.loc[:, "YearBuilt"].values.reshape(-1, 1)
X_validation = validation.loc[:, "YearBuilt"].values.reshape(-1, 1)
X_train_d2 = PolynomialFeatures(2).fit_transform(X_train)
print("X_train with degree=2:")
print(X_train_d2)
X_validation_d2 = PolynomialFeatures(2).fit_transform(X_validation)
y_train = train.loc[:, "SalePrice"].values.reshape(-1, 1)
y_validation = validation.loc[:, "SalePrice"].values.reshape(-1, 1)
reg_d1 = LinearRegression()
reg_d1.fit(X_train, y_train)
y_hat = reg_d1.predict(X_validation)
mse_d1 = mean_squared_error(y_validation, y_hat)
print("MSE with degree=1: {:.0f}".format(mse_d1))
reg_d2 = LinearRegression()
reg_d2.fit(X_train_d2, y_train)
y_hat = reg_d2.predict(X_validation_d2)
mse_d2 = mean_squared_error(y_validation, y_hat)
print("MSE with degree=2: {:.0f}".format(mse_d2))
X_arr_d1 = np.linspace(labeled["YearBuilt"].min(), labeled["YearBuilt"].max()).reshape(-1, 1)
X_arr_d2 = PolynomialFeatures(2).fit_transform(X_arr)
y_arr_d1 = reg_d1.predict(X_arr_d1)
y_arr_d2 = reg_d2.predict(X_arr_d2)
plt.scatter(train["YearBuilt"], train["SalePrice"], s=5, c="b", label="Train")
plt.scatter(validation["YearBuilt"], validation["SalePrice"], s=5, c="r", label="Validation")
plt.plot(X_arr, y_arr_d1, c="c", linewidth=3, label="d=1")
plt.plot(X_arr, y_arr_d2, c="g", linewidth=3, label="d=2")
plt.xlabel("Year Built")
plt.ylabel("Sale Price")
plt.legend(loc="upper left")
plt.show()