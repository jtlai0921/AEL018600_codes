import pandas as pd

csv_url = "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv"
df = pd.read_csv(csv_url)
df.sort_values(by=["year", "continent"], ascending=[True, False]).head() # 依照 year 遞增排序再依照 continent 遞減排序