import pandas as pd

numbers = [9, 23, 33, 91, 13]
players = ["Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley"]
df = pd.DataFrame()
df["number"] = numbers
df["player"] = players
print(df["player"])              # 解構為 Series
print(type(df["player"]))
print(df["player"].values)       # 解構為 ndarray
print(type(df["player"].values))