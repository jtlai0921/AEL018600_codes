from pyquery import PyQuery as pq
import pandas as pd
import matplotlib.pyplot as plt

def get_nba_salary():
  """
  Get NBA players' salary from ESPN.COM
  """
  player_css = "td:nth-child(2) a"
  pos_css = ".evenrow td:nth-child(2) , .oddrow td:nth-child(2)"
  salary_css = ".evenrow td:nth-child(4) , .oddrow td:nth-child(4)"
  
  nba_salary_ranking_url = "http://www.espn.com/nba/salaries/_/page/{}/seasontype/4"
  nba_salary_ranking_urls = [nba_salary_ranking_url.format(i) for i in range(1, 10)]
  players = []
  positions = []
  salaries = []
  for nba_salary_ranking_url in nba_salary_ranking_urls:
    html_doc = pq(nba_salary_ranking_url)
    player = [p.text for p in html_doc(player_css)]
    player_pos = html_doc(".evenrow td:nth-child(2) , .oddrow td:nth-child(2)").text()
    player_pos = player_pos.split(" ")
    position = []
    for pp in player_pos:
      if pp in ["C", "PF", "SF", "SG", "PG", "G"]:
        position.append(pp)
    salary = [s.text for s in html_doc(salary_css)]
    salary = [s.replace(",", "") for s in salary]
    salary = [int(s.replace("$", "")) for s in salary]
    players = players + player
    positions = positions + position
    salaries = salaries + salary
    
  df = pd.DataFrame()
  df["player"] = players
  df["position"] = positions
  df["salary"] = salaries
  
  return df

nba_salary = get_nba_salary()
fig, axes = plt.subplots(2, 3, figsize=(14, 4))

positions = nba_salary["position"].unique()
# 繪製子圖
for (ax, pos) in zip(axes.ravel(), positions):
  ax.hist(nba_salary[nba_salary["position"] == pos]["salary"], bins=15)
  ax.set_xticks([])
  ax.set_title(pos)

plt.suptitle("Player salary by positions")
plt.subplots_adjust(top=0.8)
plt.show()