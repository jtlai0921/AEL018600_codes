from pyquery import PyQuery as pq
from requests import get
import pandas as pd
import matplotlib.pyplot as plt

def get_nba_salary():
  """
  Get NBA players' salary from SPORTRAC.com
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

def get_pts_game():
  """
  Get NBA players' PTS/G from NBA.com
  """
  nba_stats_url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2017-18&SeasonType=Regular+Season&StatCategory=PTS"
  pts_game_dict = get(nba_stats_url).json()
  players = [pts_game_dict["resultSet"]["rowSet"][i][2] for i in range(len(pts_game_dict["resultSet"]["rowSet"]))]
  pts_game = [pts_game_dict["resultSet"]["rowSet"][i][22] for i in range(len(pts_game_dict["resultSet"]["rowSet"]))]
  df = pd.DataFrame()
  df["player"] = players
  df["pts_game"] = pts_game
  return df

nba_salary = get_nba_salary()
pts_game = get_pts_game()
df = pd.merge(nba_salary, pts_game)
df.plot.scatter("pts_game", "salary")
plt.show()