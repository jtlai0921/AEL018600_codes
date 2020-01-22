import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

labeled = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/Titanic-Machine-Learning-from-Disaster/train.csv")
# Removed observations without Age
labeled = labeled[~labeled["Age"].isna()]
train, validation = train_test_split(labeled, test_size=0.3, random_state=123)
X_train = train.loc[:, ["Age", "Fare"]].values
y_train = train.loc[:, "Survived"].values
# Fit Logistic regression classifier
clf = LogisticRegression()
clf.fit(X_train, y_train)
X_validation = validation.loc[:, ["Age", "Fare"]].values
y_validation = validation.loc[:, "Survived"].values
y_hat = clf.predict(X_validation)
# Calculating confusion matrix
nunique_labels = len(set(y_train))
conf_mat_shape = (nunique_labels, nunique_labels)
conf_mat = np.zeros(conf_mat_shape, dtype=int)
for actual, predict in zip(y_hat, y_validation):
  conf_mat[actual, predict] += 1
# Calculating accuracy
accuracy = (conf_mat[0, 0] + conf_mat[1, 1])/conf_mat.sum()
print(conf_mat)
print("Accuracy: {:.2f}%".format(accuracy*100))