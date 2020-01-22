# pd.read_csv() 自行指定變數的名稱
import pandas as pd

csv_url = "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
csv_df = pd.read_csv(csv_url, header=None, skiprows=1, names=['number', 'player', 'pos', 'ht', 'wt', 'birth_date', 'college'])
csv_df