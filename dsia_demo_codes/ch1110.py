import pandas as pd
import matplotlib.pyplot as plt

per_game_url = "https://storage.googleapis.com/ds_data_import/stats_per_game_chicago_bulls_1995_1996.csv"
player_info_url = "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
per_game = pd.read_csv(per_game_url)
player_info = pd.read_csv(player_info_url)
df = pd.merge(player_info, per_game[["Name", "PTS/G"]], left_on="Player", right_on="Name")
grouped = df.groupby("Pos")
points_per_game = grouped["PTS/G"].mean()

plt.bar([1, 2, 3, 4, 5], points_per_game)
plt.xticks([1, 2, 3, 4, 5], points_per_game.index)
plt.ylim(0, points_per_game.max() + 3)
plt.title("Points per game by postions")
plt.xlabel("Positions")
plt.ylabel("PPG")
for i, v in enumerate(points_per_game):
  plt.text(i + 0.9, v + 0.5, "{:.1f}".format(v))
plt.show()