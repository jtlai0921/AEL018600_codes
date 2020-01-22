import pandas as pd

numbers = [9, 23, 33, 91, 13]
players = ["Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley"]
df = pd.DataFrame()
df["number"] = numbers
df["player"] = players
toni_kukoc = pd.DataFrame()
toni_kukoc["number"] = [7]
toni_kukoc["player"] = ["Toni Kukoc"]
df = df.append(toni_kukoc)
df = df.reset_index(drop=True) # 重新設定索引
df