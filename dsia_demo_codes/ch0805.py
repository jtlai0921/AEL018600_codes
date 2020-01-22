import pandas as pd

numbers = [9, 23, 33, 91, 13]
players = ["Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley"]
weights = [185, 195, 210, 210, 265]
df = pd.DataFrame()
df["number"] = numbers
df["player"] = players
df["weight"] = weights

def get_weight_category(wt):
  if wt < 200:
    return "Light"
  elif 200 <= wt < 250:
    return "Medium"
  else:
    return "Heavy"
  
df["weight_category"] = df["weight"].map(get_weight_category)
df