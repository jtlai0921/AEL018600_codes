import pandas as pd

players = ["Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley"]
heights = ["6-6", "6-6", "6-8", "6-7", "7-2"]
weights = [185, 195, 210, 210, 265]
df = pd.DataFrame()
df["player"] = players
df["height"] = heights
df["weight"] = weights
df = df.set_index("player", drop=True) # 將球員姓名設定為列索引
long_format = df.stack()               # 寬表格轉長表格
wide_format = long_format.unstack()    # 長表格轉寬表格
wide_format