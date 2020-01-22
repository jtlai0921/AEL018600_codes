import pandas as pd

csv_url = "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv"
df = pd.read_csv(csv_url)
grouped = df.groupby(["year", "continent"])
grouped["pop"].sum().tail(n = 10)