import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

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
conf_mat = confusion_matrix(y_validation, y_hat)
# Calculating accuracy
accuracy = accuracy_score(y_validation, y_hat)
print(conf_mat)
print("Accuracy: {:.2f}%".format(accuracy*100))