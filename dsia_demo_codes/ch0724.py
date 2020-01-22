import pandas as pd

numbers = [9, 23, 33, 91, 13]
players = ["Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley"]
df = pd.DataFrame()
df["number"] = numbers
df["player"] = players
df["team"] = "Chicago Bulls"
df["height"] = ["6-6", "6-6", "6-8", "6-7", "7-2"]
df