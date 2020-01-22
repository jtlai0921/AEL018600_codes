import pandas as pd

numbers = [9, 23, 33, 91, 13]
players = ["Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley"]
df = pd.DataFrame()
df["number"] = numbers
df["player"] = players
df.index = ["PG", "SG", "SF", "PF", "C"]
df.sort_index()                # 依照索引遞增排序
df.sort_index(ascending=False) # 依照索引遞減排序