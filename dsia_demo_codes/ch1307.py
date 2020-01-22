import pandas as pd
import matplotlib.pyplot as plt

labeled_url = "https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv"
labeled_df = pd.read_csv(labeled_url)
labeled_df.plot.scatter("GrLivArea", "SalePrice")
plt.show()