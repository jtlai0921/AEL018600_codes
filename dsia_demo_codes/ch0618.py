import numpy as np

arr = np.array([True, False, 87])      # 同時有布林值與整數換為整數
print(arr)
print(arr.dtype)
print("\n")
arr = np.append(arr, 8.7)              # 同時有布林值、整數與浮點數換為浮點數
print(arr)
print(arr.dtype)
print("\n")
arr = np.append(arr, "Luke Skywalker") # 同時有布林值、整數、浮點數與文字換為文字
print(arr)
print(arr.dtype)