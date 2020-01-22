import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996_per_game.csv")
df_numerics = df.iloc[:, 4:]
corr_matrix = df_numerics.corr()
sns.heatmap(corr_matrix)
plt.show()