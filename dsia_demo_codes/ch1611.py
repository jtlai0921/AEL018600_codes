import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def sigmoid(z):
  return 1/(1 + np.exp(-z))

digits = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/Digit-Recognizer/train.csv")
unique_digits = digits["label"].unique()
unique_digits.sort()
train, validation = train_test_split(digits, test_size=0.3, random_state=123)
X_train = train.loc[:, "pixel0":"pixel783"].values
X_valid = validation.loc[:, "pixel0":"pixel783"].values
ones = np.ones(X_valid.shape[0]).reshape(-1, 1)
X_valid = np.concatenate([ones, X_valid], axis=1)
y_train = train.loc[:, "label"].values
# One vs. all
all_probs = np.zeros((X_valid.shape[0], unique_digits.size))
for digit_label in unique_digits:
  y_train_recoded = np.where(y_train == digit_label, 1, 0)
  clf = LogisticRegression()
  clf.fit(X_train, y_train_recoded)
  thetas = np.concatenate([clf.intercept_.reshape(-1, 1), clf.coef_.reshape(-1, 1)])
  y_prob = sigmoid(np.dot(X_valid, thetas))
  all_probs[:, digit_label] = y_prob.ravel()
print(all_probs.argmax(axis=1))