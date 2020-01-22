import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
  
labeled_url = "https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv"
labeled_df = pd.read_csv(labeled_url)
train_df, validation_df = train_test_split(labeled_df, test_size=0.3, random_state=123)
X_train = train_df["GrLivArea"].values.reshape(-1, 1)
y_train = train_df["SalePrice"].values.reshape(-1, 1)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
theta_0 = regressor.intercept_[0]
theta_1 = regressor.coef_[0, 0]
X_min = labeled_df["GrLivArea"].min()
X_max = labeled_df["GrLivArea"].max()
X_arr = np.linspace(X_min, X_max)
y_hats = theta_0 + theta_1 * X_arr

plt.scatter(train_df["GrLivArea"], train_df["SalePrice"], color="r", s=5, label="train")
plt.scatter(validation_df["GrLivArea"], validation_df["SalePrice"], color="g", s=5, label="validation")
plt.plot(X_arr, y_hats, color="c", linewidth=3, label="h")
plt.legend(loc="upper left")
plt.xlabel("Ground Living Area")
plt.ylabel("Sale Price")
plt.show()