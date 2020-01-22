# pd.read_csv() 使用預設參數
import pandas as pd

csv_url = "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
csv_df = pd.read_csv(csv_url)
csv_df