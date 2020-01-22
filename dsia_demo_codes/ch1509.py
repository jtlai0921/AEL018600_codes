import numpy as np

def sigmoid(z):
  return 1/(1 + np.exp(-z))

def gradient(X, y, thetas):
  m = y.size
  h = sigmoid(X.dot(thetas.reshape(-1,1)))
  grad =(1/m)*X.T.dot(h-y)
  return(grad.ravel())