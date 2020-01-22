import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import RidgeClassifier

def sigmoid(z):
  return 1/(1 + np.exp(-z))

def step(g_y_hat, threshold=0.5):
  return np.where(g_y_hat >= threshold, 1, 0).reshape(-1, 1)

def plot_decision_boundary(xlab, ylab, thetas, labeled, pos_label="Survived", neg_label="Dead", clf_target="Survived", poly_d=6, axes=None):
  xx_min, xx_max = labeled[xlab].min(), labeled[xlab].max()
  yy_min, yy_max = labeled[ylab].min(), labeled[ylab].max()
  xx_arr = np.linspace(xx_min - 5, xx_max + 5, 1000)
  yy_arr = np.linspace(yy_min - 5, yy_max + 5, 1000)
  xx, yy = np.meshgrid(xx_arr, yy_arr)
  X_grid = np.concatenate([xx.reshape(-1, 1), yy.reshape(-1, 1)], axis=1)
  X_grid_poly = PolynomialFeatures(poly_d).fit_transform(X_grid)
  Z = step(sigmoid(np.dot(X_grid_poly, thetas))).reshape(xx.shape)
  pos = labeled[labeled[clf_target] == 1]
  neg = labeled[labeled[clf_target] == 0]
  if axes == None:
    axes = plt.gca()
  axes.scatter(pos[xlab], pos[ylab], label=pos_label, marker="o", color="blue")
  axes.scatter(neg[xlab], neg[ylab], label=neg_label, marker="x", color="red")
  axes.contourf(xx, yy, Z, alpha=0.4, cmap=plt.cm.coolwarm_r)
  axes.legend()
  axes.set_xlabel(xlab)
  axes.set_ylabel(ylab)

labeled = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/Titanic-Machine-Learning-from-Disaster/train.csv")
# Removed observations without Age
labeled = labeled[~labeled["Age"].isna()]
train, validation = train_test_split(labeled, test_size=0.3, random_state=123)
X_train = train.loc[:, ["Fare", "Age"]].values
X_train_poly = PolynomialFeatures(6).fit_transform(X_train)
y_train = train.loc[:, "Survived"].values
ridge_clf = RidgeClassifier()
ridge_clf.fit(X_train_poly, y_train)
thetas = np.concatenate([ridge_clf.intercept_.reshape(-1, 1), ridge_clf.coef_[0, 1:].reshape(-1, 1)])

# Decision boundary plots
fig, axes = plt.subplots(2, 3, sharey=True, figsize=(17, 10))
for i, alpha in enumerate([0, 1, 1e3, 1e6, 1e9, 1e12]):
  ridge_clf = RidgeClassifier(alpha=alpha)
  ridge_clf.fit(X_train_poly, y_train)
  thetas = np.concatenate([ridge_clf.intercept_.reshape(-1, 1), ridge_clf.coef_[0, 1:].reshape(-1, 1)])
  plot_decision_boundary("Fare", "Age", thetas, labeled, axes=axes.ravel()[i])
  axes.ravel()[i].set_title("Lambda: {:.0e}".format(ridge_clf.alpha))
plt.tight_layout()