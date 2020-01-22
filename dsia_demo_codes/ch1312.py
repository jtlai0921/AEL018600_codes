import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def compute_cost(X, y, thetas):
  m = X.shape[0]
  h = np.dot(X, thetas)
  J = 1/(2*m)*np.sum(np.square(h - y))
  return J
  
def get_thetas_lm(X, y, alpha=0.001, num_iters=10000):
  thetas = np.array([0, 0]).reshape(-1, 1)
  X = X.reshape(-1, 1)
  y = y.reshape(-1, 1)
  m = X.shape[0]
  ones = np.ones(m, dtype=int).reshape(-1, 1)
  X = np.concatenate([ones, X], axis=1)
  J_history = np.zeros(num_iters)
  for num_iter in range(num_iters):
    h = np.dot(X, thetas)
    loss = h - y
    gradient = np.dot(X.T, loss)
    thetas = thetas - (alpha * gradient)/m
    J_history[num_iter] = compute_cost(X, y, thetas=thetas)
  return thetas, J_history

def get_rescaled_thetas(thetas, scaler_X, scaler_y, X_train, y_train):
  theta_0 = thetas[0, 0]
  theta_1 = thetas[1, 0]
  scale_X = scaler_X.scale_[0]
  scale_y = scaler_y.scale_[0]
  theta_0_rescaled = y_train.mean() + y_train.std()*theta_0 - theta_1*X_train.mean()*(y_train.std()/X_train.std())
  theta_1_rescaled = theta_1 / scale_X * scale_y
  return theta_0_rescaled, theta_1_rescaled
  
labeled_url = "https://storage.googleapis.com/kaggle_datasets/House-Prices-Advanced-Regression-Techniques/train.csv"
labeled_df = pd.read_csv(labeled_url)
train_df, validation_df = train_test_split(labeled_df, test_size=0.3, random_state=123)
X_train = train_df["GrLivArea"].values.reshape(-1, 1).astype(float)
y_train = train_df["SalePrice"].values.reshape(-1, 1).astype(float)
# Normalization
scaler_X = StandardScaler()
scaler_y = StandardScaler()
X_train_scaled = scaler_X.fit_transform(X_train)
y_train_scaled = scaler_y.fit_transform(y_train)
thetas, J_history = get_thetas_lm(X_train_scaled, y_train_scaled)
# Rescaling
theta_0, theta_1 = get_rescaled_thetas(thetas, scaler_X, scaler_y, X_train, y_train)
print("Theta 0: {:.4f}".format(theta_0))
print("Theta 1: {:.4f}".format(theta_1))
# Plotting J_history
plt.plot(J_history)
plt.title("Cost function during gradient descent")
plt.xlabel("Iterations")
plt.ylabel(r"$J(\theta)$")
plt.show()