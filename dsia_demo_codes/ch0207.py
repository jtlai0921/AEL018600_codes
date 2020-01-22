# pd.read_excel() 使用預設參數
import pandas as pd

xlsx_url = "https://storage.googleapis.com/ds_data_import/fav_nba_teams.xlsx"
chicsgo_bulls = pd.read_excel(xlsx_url)
chicsgo_bulls