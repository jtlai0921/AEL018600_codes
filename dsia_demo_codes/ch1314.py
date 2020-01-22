import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
  
labeled_url = "https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv"
labeled_df = pd.read_csv(labeled_url)
train_df, validation_df = train_test_split(labeled_df, test_size=0.3, random_state=123)
X_train = train_df["GrLivArea"].values.reshape(-1, 1)
y_train = train_df["SalePrice"].values.reshape(-1, 1)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
theta_0 = regressor.intercept_[0]
theta_1 = regressor.coef_[0, 0]
print("Theta 0: {:.4f}".format(theta_0))
print("Theta 1: {:.4f}".format(theta_1))