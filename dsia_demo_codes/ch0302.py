import pandas as pd
from sqlalchemy import create_engine

csv_url = "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
chicago_bulls = pd.read_csv(csv_url)
host = "YOURHOST" # 輸入自己的 AWS RDS Enpoint 位址
port = 3306
dbname = "YOURDBNAME" # 輸入自己設定的資料庫名稱
user = "YOURUSERNAME" # 輸入自己設定的使用者名稱
password = "YOURPASSWORD" # 輸入自己設定的使用者密碼

engine = create_engine('mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}'.format(user=user, password=password, host=host, port=port, dbname=dbname))
chicago_bulls.to_sql('chicago_bulls', engine, index=False, if_exists='replace')