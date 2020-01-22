from google.cloud import bigquery
import pandas as pd
from pandas_gbq import to_gbq

csv_url = "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
chicago_bulls = pd.read_csv(csv_url, header=None, skiprows=1, names=['number', 'player', 'pos', 'ht', 'wt', 'birth_date', 'college'])
to_gbq(chicago_bulls, destination_table='fav_nba_teams.chicago_bulls', project_id='YOURPROJECTID', if_exists='replace', private_key='YOURSERVICEACCOUNT')