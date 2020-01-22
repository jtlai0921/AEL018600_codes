import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import PolynomialFeatures

def plot_decision_boundary(xlab, ylab, clf, labeled, pos_label="Survived", neg_label="Dead", clf_target="Survived", degree=1):
  xx_min, xx_max = labeled[xlab].min(), labeled[xlab].max()
  yy_min, yy_max = labeled[ylab].min(), labeled[ylab].max()
  xx_arr = np.linspace(xx_min - 5, xx_max + 5, 1000)
  yy_arr = np.linspace(yy_min - 5, yy_max + 5, 1000)
  xx, yy = np.meshgrid(xx_arr, yy_arr)
  X_grid = np.concatenate([xx.reshape(-1, 1), yy.reshape(-1, 1)], axis=1)
  X_grid_poly = PolynomialFeatures(degree).fit_transform(X_grid)
  Z = clf.predict(X_grid_poly).reshape(xx.shape)
  pos = labeled[labeled[clf_target] == 1]
  neg = labeled[labeled[clf_target] == 0]
  plt.scatter(pos[xlab], pos[ylab], label=pos_label, marker="o", color="blue")
  plt.scatter(neg[xlab], neg[ylab], label=neg_label, marker="x", color="red")
  plt.contourf(xx, yy, Z, alpha=0.4, cmap=plt.cm.coolwarm_r)
  plt.legend()
  plt.xlabel(xlab)
  plt.ylabel(ylab)

labeled = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/Titanic-Machine-Learning-from-Disaster/train.csv")
# Removed observations without Age
labeled = labeled[~labeled["Age"].isna()]
train, validation = train_test_split(labeled, test_size=0.3, random_state=123)
X_train = train.loc[:, ["Fare", "Age"]].values
# Polynomial features
d = 6
X_train_poly = PolynomialFeatures(d).fit_transform(X_train)
y_train = train.loc[:, "Survived"].values
# Fit Logistic regression classifier
clf = LogisticRegression()
clf.fit(X_train_poly, y_train)
# Decision boundary plot
plot_decision_boundary("Fare", "Age", clf, labeled, degree=d)
plt.show()