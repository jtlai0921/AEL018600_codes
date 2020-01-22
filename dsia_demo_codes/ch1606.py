import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import cross_val_score

labeled = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/Titanic-Machine-Learning-from-Disaster/train.csv")
# Removed observations without Age
labeled = labeled[~labeled["Age"].isna()]
X = labeled.loc[:, ["Fare", "Age"]].values
y = labeled.loc[:, "Survived"].values
d = 10
poly_degrees = list(range(1, d+1))
cv_accuracies = []
for poly_d in poly_degrees:
  X_poly = PolynomialFeatures(poly_d).fit_transform(X)
  # Get cross validated train/valid accuracy
  clf = LogisticRegression()
  cv_acc = np.array(cross_val_score(clf, X_poly, y)).mean()
  cv_accuracies.append(cv_acc)

plt.plot(cv_accuracies, marker="o")
plt.xticks(range(d), poly_degrees)
plt.title("Cross-validated accuracies")
plt.xlabel("Degrees")
plt.ylabel("CV Accuracy")
plt.show()