import pandas as pd
import matplotlib.pyplot as plt

csv_url = "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
df = pd.read_csv(csv_url)
grouped = df.groupby("Pos")
pos = grouped["Pos"].count()

plt.bar(range(1, 6), pos)
plt.xticks(range(1, 6), pos.index)
plt.suptitle("Front court players are the majorities.")
plt.title("Chicago Bulls is relatively weak in the paint.")
plt.xlabel("Positions")
plt.ylabel("Number of Players")
plt.show()