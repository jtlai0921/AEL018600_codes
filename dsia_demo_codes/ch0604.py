import numpy as np

arr = np.array([11, 12, 13, 14, 15])

print(arr[0])         # 選最左邊
print(arr[-1])        # 選最右邊
print(arr[[0, 1, 4]]) # 不規則地選擇片段