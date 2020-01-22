# pd.read_excel() 指定工作表與讀取範圍
import pandas as pd

xlsx_url = "https://storage.googleapis.com/ds_data_import/fav_nba_teams.xlsx"
boston_celtics = pd.read_excel(xlsx_url, sheet_name='boston_celtics_2007_2008', skiprows=6, header=None, names=['number', 'player', 'pos'], usecols=[0, 1, 2])
boston_celtics