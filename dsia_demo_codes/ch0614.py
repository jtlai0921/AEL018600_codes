import numpy as np

arr = np.array([11, 12, 13, 14, 15])
is_even = arr % 2 == 0
print(is_even)
print(arr[is_even])