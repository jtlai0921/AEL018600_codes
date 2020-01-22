import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

labeled = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv")
train, validation = train_test_split(labeled, test_size=0.3, random_state=123)
plt.scatter(train["YearBuilt"], train["SalePrice"], s=5, c="b", label="Train")
plt.scatter(validation["YearBuilt"], validation["SalePrice"], s=5, c="r", label="Validation")
plt.xlabel("Year Built")
plt.ylabel("Sale Price")
plt.legend(loc="upper left")
plt.show()