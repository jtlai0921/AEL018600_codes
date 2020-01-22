import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
  return 1/(1 + np.exp(-z))

x_arr = np.linspace(-10, 10)
y_arr = np.array(list(map(sigmoid, x_arr)))
plt.plot(x_arr, y_arr)
plt.xticks([-10, 0, 10], ["$-\infty$", "$0$", "$\infty$"])
plt.yticks([0, 0.5, 1], ["0", "0.5", "1"])
plt.xlabel("$X\\theta$")
plt.ylabel("$g(X\\theta)$")
plt.title("Sigmoid Function")
plt.show()