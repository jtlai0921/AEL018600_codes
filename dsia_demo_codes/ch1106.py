import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

csv_url = "https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.csv"
df = pd.read_csv(csv_url)
grouped = df.groupby("Pos")
pos = grouped["Pos"].count()

# 可以顯示中文
myfont = FontProperties(fname="/System/Library/Fonts/STHeiti Light.ttc")
plt.bar(range(1, 6), pos)
plt.xticks(range(1, 6), ["中鋒", "大前鋒", "小前鋒",
                         "控球後衛", "得分後衛"], fontproperties=myfont)
plt.suptitle("前場球員為芝加哥公牛隊的大宗", fontproperties=myfont)
plt.title("反映當時為了抗衡其他具有主宰力中前鋒的隊伍之現象", fontproperties=myfont)
plt.xlabel("鋒衛位置", fontproperties=myfont)
plt.ylabel("球員人數", fontproperties=myfont)
plt.show()
