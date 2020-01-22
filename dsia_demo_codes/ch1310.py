import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def get_thetas_lm(X, y):
  m = X.size
  X = X.reshape(-1, 1)
  y = y.reshape(-1, 1)
  ones = np.ones(m, dtype=int).reshape(-1, 1)
  X = np.concatenate([ones, X], axis=1)
  LHS = np.dot(X.T, X)
  RHS = np.dot(X.T, y)
  LHS_inv = np.linalg.inv(LHS)
  thetas = np.dot(LHS_inv, RHS)
  return tuple(thetas.ravel())

labeled_url = "https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv"
labeled_df = pd.read_csv(labeled_url)
train_df, validation_df = train_test_split(labeled_df, test_size=0.3, random_state=123)
X_train = train_df["GrLivArea"].values
y_train = train_df["SalePrice"].values
theta_0, theta_1 = get_thetas_lm(X_train, y_train)
print("Theta 0: {:.4f}".format(theta_0))
print("Theta 1: {:.4f}".format(theta_1))