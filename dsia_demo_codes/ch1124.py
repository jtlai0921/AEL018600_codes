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
nba_salary[nba_salary["position"] == "PG"]["salary"].plot.hist(bins = 15, label = "PG")
nba_salary[nba_salary["position"] == "SG"]["salary"].plot.hist(bins = 15, label = "SG")
nba_salary[nba_salary["position"] == "G"]["salary"].plot.hist(bins = 15, label = "G")
nba_salary[nba_salary["position"] == "SF"]["salary"].plot.hist(bins = 15, label = "SF")
nba_salary[nba_salary["position"] == "PF"]["salary"].plot.hist(bins = 15, label = "PF")
nba_salary[nba_salary["position"] == "C"]["salary"].plot.hist(bins = 15, label = "C")
plt.legend()
plt.title("Player salary by positions")
plt.xlabel("Salary")
plt.show()