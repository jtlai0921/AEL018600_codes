import pandas as pd
import matplotlib.pyplot as plt

labeled = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/Titanic-Machine-Learning-from-Disaster/train.csv")
# Removed observations without Age
labeled = labeled[~labeled["Age"].isna()]
survived = labeled[labeled["Survived"] == 1]
dead = labeled[labeled["Survived"] == 0]
plt.scatter(survived["Fare"], survived["Age"], label="Survived", color="blue", marker="o", alpha=0.5)
plt.scatter(dead["Fare"], dead["Age"], label="Dead", color="red", marker="x", alpha=0.5)
plt.xlabel("Fare")
plt.ylabel("Age")
plt.legend()
plt.show()