# treemap
import pandas as pd
import matplotlib.pyplot as plt
import squarify

csv_url = "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
df = pd.read_csv(csv_url)
grouped = df.groupby("Pos")
pos = grouped["Pos"].count()
squarify.plot(sizes=pos.values, label=pos.index, color=["red", "green", "blue", "grey", "yellow"], alpha=0.4)
plt.axis('off')
plt.title("1995-1996 Chicago Bulls roster")
plt.show()