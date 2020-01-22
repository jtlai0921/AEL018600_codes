from pyquery import PyQuery as pq
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_nba_salary():
  """
  Get NBA players' salary from SPORTRAC.COM
  """
  nba_salary_ranking_url = "https://www.spotrac.com/nba/rankings/"
  html_doc = pq(nba_salary_ranking_url)
  player_css = ".team-name"
  pos_css = ".rank-position"
  salary_css = ".info"
  players = [p.text for p in html_doc(player_css)]
  positions = [p.text for p in html_doc(pos_css)]
  salaries = [s.text.replace("$", "") for s in html_doc(salary_css)]
  salaries = [int(s.replace(",", "")) for s in salaries]
  df = pd.DataFrame()
  df["player"] = players
  df["pos"] = positions
  df["salary"] = salaries
  return df

nba_salary = get_nba_salary()
fig, axes = plt.subplots(2, 3)
wide_format = nba_salary.pivot(index='player', columns='pos', values='salary')
colors = ["r", "g", "b", "c", "m"]
positions = nba_salary["pos"].unique()
ax_rows = [0, 0, 0, 1, 1]
ax_cols = [0, 1, 2, 0, 1]
for pos, color, ax_row, ax_col in zip(positions, colors, ax_rows, ax_cols):
  sns.kdeplot(wide_format[pos][wide_format[pos].notna()], shade=True, color=color, alpha = 0.5, ax=axes[ax_row, ax_col], legend=False)
  axes[ax_row, ax_col].set_title(pos)

axes[1, 2].set_visible(False) # hiding the sixth subplot
fig.suptitle("Salary of NBA players by positions")
fig.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()