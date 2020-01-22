import pandas as pd
import matplotlib.pyplot as plt

csv_url = "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
df = pd.read_csv(csv_url)
grouped = df.groupby("Pos")
pos = grouped["Pos"].count()
plt.bar([1, 2, 3, 4, 5], pos)
plt.xticks([1, 2, 3, 4, 5], pos.index)
plt.yticks([1, 2, 3, 4], [1, 2, 3, 4])
plt.show()