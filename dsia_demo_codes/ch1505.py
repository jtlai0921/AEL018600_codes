import numpy as np
import matplotlib.pyplot as plt

x_arr = np.linspace(0, 1)
y_arr_0 = -np.log(x_arr)
y_arr_1 = -np.log(1 - x_arr)
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(x_arr, y_arr_0)
axes[0].set_title("$y=1,-\log(g(\hat{y}))}$")
axes[0].set_xlabel("$g(\hat{y})$")
axes[1].plot(x_arr, y_arr_1)
axes[1].set_title("$y=0, -\log(1 - g(\hat{y}))$")
axes[1].set_xlabel("$g(\hat{y})$")
plt.show()