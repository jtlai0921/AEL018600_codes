import pandas as pd
import matplotlib.pyplot as plt

csv_url = "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
df = pd.read_csv(csv_url)
grouped = df.groupby("Pos")
pos = grouped.count()
bar_1 = pos["Player"].loc[["SG", "PG"]].values
bar_2 = pos["Player"].loc[["SF", "PF", "C"]].values
plt.bar(range(1, 3), bar_1, label="Back Court", alpha=0.6, color="red")
plt.bar(range(3, 6), bar_2, label="Front Court", alpha=0.6, color="green")
plt.legend(title = "Court") # 加入圖例
plt.xticks(range(1, 6), ["SG", "PG", "SF", "PF", "C"]) # 調整 X 軸刻度線與刻度線標籤
plt.yticks(range(1, 5)) # 調整 Y 軸刻度線與刻度線標籤
plt.suptitle("Front court players are the majorities.")
plt.title("Chicago Bulls is relatively weak in the paint.")
plt.xlabel("Positions")
plt.ylabel("Number of Players")
plt.show()