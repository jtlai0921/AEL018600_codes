from pyquery import PyQuery as pq
import pandas as pd
import matplotlib.pyplot as plt

def get_pp_stats():
  """
  Get Paul Pierce stats from basketball-reference.com
  """
  stats_url = "https://www.basketball-reference.com/players/p/piercpa01.html"
  html_doc = pq(stats_url)
  pts_css = "#per_game .full_table .right:nth-child(30)"
  ast_css = "#per_game .full_table .right:nth-child(25)"
  reb_css = "#per_game .full_table .right:nth-child(24)"
  year = [str(i)+"-01-01" for i in range(1999, 2018)]
  pts = [float(p.text) for p in html_doc(pts_css)]
  ast = [float(a.text) for a in html_doc(ast_css)]
  reb = [float(r.text) for r in html_doc(reb_css)]
  df = pd.DataFrame()
  df["year"] = year
  df["pts"] = pts
  df["ast"] = ast
  df["reb"] = reb
  return df

pp_stats = get_pp_stats()
pp_stats["year"] = pd.to_datetime(pp_stats["year"])
pp_stats = pp_stats.set_index("year")
plt.plot(pp_stats["pts"]) # 線圖
avg_pts = pp_stats["pts"].mean() # 生涯均值
plt.axhline(y = avg_pts, color="g", ls="--", alpha = 0.5) # 水平線
plt.fill_between(pp_stats.index, avg_pts, pp_stats["pts"], 
                 where=pp_stats["pts"] >= avg_pts, color="gray",
                 alpha=0.5, interpolate=True) # 陰影

year_2013 = pp_stats.index[-5] # 2013 年的 index
# 加入箭號與註釋文字
plt.annotate(
    'Left Boston Celtics',
    xy=(year_2013, 19),
    xycoords='data',
    xytext=(year_2013, 25),
    textcoords='data',
    horizontalalignment='center',
    arrowprops=dict(facecolor='black', arrowstyle="fancy")
)
plt.title("Points per game: Paul Pierce")
plt.xlabel("Year")
plt.ylabel("PPG")
plt.show()