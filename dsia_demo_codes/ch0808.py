import pandas as pd
import numpy as np

numbers = [9, 23, 33, 91, 13, 7]
players = ["Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley", "Toni Kukoc"]
colleges = ["Miami University", "University of North Carolina", "University of Central Arkansas", "Southeastern Oklahoma State University", "University of New Mexico", np.nan] # np.nan 替換為 None 亦可
df = pd.DataFrame()
df["number"] = numbers
df["player"] = players
df["college"] = colleges
print(df["college"].notna()) # 判斷大學是否無遺漏值
df[df["college"].notna()]    # 篩選出大學非遺漏值的列數