import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

per_game_url = "https://storage.googleapis.com/ds_data_import/stats_per_game_chicago_bulls_1995_1996.csv"
player_info_url = "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
per_game = pd.read_csv(per_game_url)
player_info = pd.read_csv(player_info_url)
df = pd.merge(player_info, per_game[["Name", "PTS/G"]], left_on="Player", right_on="Name")
grouped = df.groupby("Pos")
points_per_game = grouped["PTS/G"].mean()
points_per_game = points_per_game.sort_values()
sns.set_style("white")
plt.plot(points_per_game, range(1, points_per_game.size + 1), 'o')
plt.hlines(y=range(1, points_per_game.size + 1), xmin=0, xmax=points_per_game, color='skyblue')
plt.yticks(range(1, points_per_game.size + 1), points_per_game.index)
plt.xlim(0, 33)
for i, v in enumerate(points_per_game):
  plt.text(v + 0.5, i + 0.95, "{:.1f}".format(v))
plt.title("1995-1996 Chicago Bulls PPG by positions")
plt.show()