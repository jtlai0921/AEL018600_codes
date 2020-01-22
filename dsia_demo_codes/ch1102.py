import pandas as pd
import matplotlib.pyplot as plt

csv_url = "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
df = pd.read_csv(csv_url)
grouped = df.groupby("Pos")
pos = grouped["Pos"].count()
plt_themes = ["seaborn-darkgrid", "ggplot", "dark_background", "bmh", "fivethirtyeight"]

for i in range(5):
  plt.style.use(plt_themes[i])
  plt.bar(range(1, 6), pos)
  plt.xticks(range(1, 6), pos.index)
  plt.title(plt_themes[i])
  plt.show()
  print("\n")