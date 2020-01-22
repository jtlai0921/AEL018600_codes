import pandas as pd

csv_url = "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv"
gapminder = pd.read_csv(csv_url)
nrows, ncols = gapminder.shape
min_year = gapminder["year"].min()
max_year = gapminder["year"].max()
year_interval = gapminder["year"].unique()[1] - gapminder["year"].unique()[0]
ncountries = gapminder["country"].nunique()
msg = "這個摘錄版本僅有 {} 個觀測值、{} 個變數，涵括 {} 至 {} 年中每 {} 年、{} 個國家的快照"

print("變數名稱：")
print(list(gapminder.columns))
print(msg.format(nrows, ncols, min_year, max_year, year_interval, ncountries))