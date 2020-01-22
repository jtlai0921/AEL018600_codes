import pandas as pd

numbers = [9, 23, 33, 91, 13]
players = ["Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley"]
birth_dates = ["January 20, 1964", "February 17, 1963", "September 25, 1965", "May 13, 1961", "January 19, 1969"]
df = pd.DataFrame()
df["number"] = numbers
df["player"] = players
df["birth_date"] = birth_dates
print(df["birth_date"].dtype) # 字元型別
df