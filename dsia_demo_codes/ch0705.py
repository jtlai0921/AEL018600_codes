import pandas as pd

csv_url = "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv"
df = pd.read_csv(csv_url)
df.head()     # 查看前五列觀測值
df.tail()     # 查看末五列觀測值
df.info()     # 查看資料框的複合資訊
df.describe() # 查看數值變數的描述性統計
df.shape      # 查看資料框的外觀