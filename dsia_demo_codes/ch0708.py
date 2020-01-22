import pandas as pd

numbers = [9, 23, 33, 91, 13]
players = ["Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley"]
df = pd.DataFrame()
df["number"] = numbers
df["player"] = players
df.index = ["PG", "SG", "SF", "PF", "C"]
df.loc[["SG", "SF", "PF"], ["number", "player"]] # 以索引為準
df.iloc[[1, 2, 3], [0, 1]]                       # 以位置為準