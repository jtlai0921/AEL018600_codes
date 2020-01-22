import numpy as np

arr = np.array([11, 12, 13, 14, 15])
arr = np.delete(arr, 2) # 刪除位於索引值 2 的 13
print(arr)