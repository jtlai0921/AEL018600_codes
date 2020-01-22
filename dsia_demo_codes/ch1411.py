import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

labeled = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv")
train, validation = train_test_split(labeled, test_size=0.3, random_state=123)
X_train_simple = train.loc[:, "GrLivArea"].values.reshape(-1, 1)
X_train_multiple = train.loc[:, ["GrLivArea", "GarageArea"]].values
y_train = train.loc[:, "SalePrice"].values.reshape(-1, 1)
X_validation_simple = validation.loc[:, "GrLivArea"].values.reshape(-1, 1)
X_validation_multiple = validation.loc[:, ["GrLivArea", "GarageArea"]].values
y_validation = validation.loc[:, "SalePrice"].values.reshape(-1, 1)
reg_simple = LinearRegression()
reg_multiple = LinearRegression()
reg_simple.fit(X_train_simple, y_train)
reg_multiple.fit(X_train_multiple, y_train)
y_hat_simple = reg_simple.predict(X_validation_simple)
y_hat_multiple = reg_multiple.predict(X_validation_multiple)
mse_simple = mean_squared_error(y_validation, y_hat_simple)
mse_multiple = mean_squared_error(y_validation, y_hat_multiple)
print("MSE of simple linear regression: {:.0f}".format(mse_simple))
print("MSE of multiple linear regression: {:.0f}".format(mse_multiple))