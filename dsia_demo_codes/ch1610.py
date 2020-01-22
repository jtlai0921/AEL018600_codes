import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

digit_recognizer = pd.read_csv("https://storage.googleapis.com/kaggle_datasets/Digit-Recognizer/train.csv")
fig, axes = plt.subplots(10, 10, figsize=(8, 8))
fig.subplots_adjust(hspace=0.1, wspace=0.1)

for i, ax in enumerate(axes.flat):
  digit = digit_recognizer.iloc[i, 1:].values.reshape(28, 28)
  ax.imshow(digit, cmap='binary', interpolation='nearest')
  ax.text(0.05, 0.05, str(digit_recognizer["label"][i]),
          transform=ax.transAxes, color='green')
  ax.set_xticks([])
  ax.set_yticks([])