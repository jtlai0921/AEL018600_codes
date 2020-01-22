import numpy as np

def sigmoid(z):
  return 1/(1 + np.exp(-z))

def cost_function(X, y, thetas):
  m = X.shape[0]
  h = sigmoid(X.dot(thetas))
  J = -1*(1/m)*(np.log(h).T.dot(y)+np.log(1-h).T.dot(1-y))
  # log(0) approached -Inf results in NaN
  if np.isnan(J[0]):
    return(np.inf)
  else:
    return(J[0])