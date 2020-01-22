import numpy as np

arr = np.array([11, 12, 13, 14, 15])
for idx, val in enumerate(arr):
  print("位於索引值 {} 的數字是 {}".format(idx, val))