import numpy as np

vec = np.array([11, 12, 13, 14, 15]).reshape(5, 1)
mat = np.arange(11, 21).reshape(2, 5)
tensor = np.arange(11, 35).reshape(2, 3, 4)

print(vec[vec % 2 == 0])
print(mat[mat % 2 == 0])
print(tensor[tensor % 2 == 0])