import pandas as pd

numbers = [9, 23, 33, 91, 13]
players = ["Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley"]
df = pd.DataFrame()
df["number"] = numbers
df["player"] = players
df.index = ["PG", "SG", "SF", "PF", "C"]
is_trio = df["player"].isin(["Michael Jordan", "Scottie Pippen", "Dennis Rodman"]) # 透過球員姓名
print(is_trio)
df[is_trio]