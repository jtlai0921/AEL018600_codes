import pandas as pd
import numpy as np

numbers = [9, 23, 33, 91, 13, 7]
players = ["Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley", "Toni Kukoc"]
colleges = ["Miami University", "University of North Carolina", "University of Central Arkansas", "Southeastern Oklahoma State University", "University of New Mexico", None] # None 替換為 np.nan 亦可
df = pd.DataFrame()
df["number"] = numbers
df["player"] = players
df["college"] = colleges
df