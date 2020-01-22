import pandas as pd

labeled_url = "https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv"
labeled_df = pd.read_csv(labeled_url)
df_corr = labeled_df.corr()
sale_price_corr = df_corr["SalePrice"].abs().sort_values(ascending=False)
sale_price_corr[sale_price_corr >= 0.6]