import pandas as pd

numbers = [9, 23, 33, 91, 13]
players = ["Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley"]
df = pd.DataFrame()
df["number"] = numbers
df["player"] = players
position_dict = {
    "Ron Harper": "PG",
    "Michael Jordan": "SG",
    "Scottie Pippen": "SF",
    "Dennis Rodman": "PF",
    "Luc Longley": "C"
}
df["position"] = df["player"].map(position_dict)
df