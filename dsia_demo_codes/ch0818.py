import pandas as pd

players = ["Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley"]
numbers = [9, 23, 33, 91, 13]
colleges = ["Miami University", "University of North Carolina", "University of Central Arkansas", "Southeastern Oklahoma State University", "University of New Mexico"]
number_df = pd.DataFrame()
number_df["player"] = players
number_df["number"] = numbers
college_df = pd.DataFrame()
college_df["player"] = players
college_df["college"] = colleges
pd.merge(number_df, college_df, on='player')