from pyquery import PyQuery as pq
import pandas as pd
import matplotlib.pyplot as plt

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
plt.hist(nba_salary["salary"], bins=15)
plt.show()