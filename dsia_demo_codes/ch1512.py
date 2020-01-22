import numpy as np
import matplotlib.pyplot as plt
  
x_arr_0 = np.arange(0, 0.5, 0.01)
x_arr_1 = np.arange(0.5, 1, 0.01)
y_arr_0 = np.where(x_arr_0 >= 0.5, 1, 0)
y_arr_1 = np.where(x_arr_1 >= 0.5, 1, 0)
plt.plot(x_arr_0, y_arr_0, color="b")
plt.plot(x_arr_1, y_arr_1, color="b")
plt.scatter([0.5], [0], facecolors='none', edgecolors='b')
plt.scatter([0.5], [1], color='b')
plt.xticks([0, 0.5, 1])
plt.yticks([0, 1])
plt.xlabel("$g(X\\theta)$")
plt.title("Step Function")
plt.show()