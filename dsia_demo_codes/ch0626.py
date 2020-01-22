import numpy as np

vec = np.array([11, 12, 13, 14, 15]).reshape(5, 1)
mat = np.arange(11, 21).reshape(2, 5)
tensor = np.arange(11, 35).reshape(2, 3, 4)

print(vec[4, 0])       # 15 位於 (4, 0)    
print(mat[0, 4])       # 15 位於 (0, 4)
print(tensor[0, 1, 0]) # 15 位於 (0, 1, 0)