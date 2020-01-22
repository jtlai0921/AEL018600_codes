# pd.read_table() 指定 sep=";"
import pandas as pd

txt_url = "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.txt"
txt_df = pd.read_table(txt_url, sep=";")
txt_df