import numpy as np

arr = np.array([11, 12, 13, 14, 15])
arr = np.append(arr, 87)    # 在陣列的尾端加入 87
arr = np.insert(arr, 1, 99) # 在索引值 1 的位置加入 99
print(arr)