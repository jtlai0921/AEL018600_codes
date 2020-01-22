import numpy as np

def sigmoid(z):
  return 1/(1 + np.exp(-z))

def cost_function_regularized(X, y, thetas, Lambda):
  m = y.size
  h = sigmoid(X.dot(thetas))
  J = -1*(1/m)*(np.log(h).T.dot(y)+np.log(1-h).T.dot(1-y)) + (Lambda/(2*m))*np.sum(np.square(thetas[1:]))
  if np.isnan(J):
    return np.inf
  else:
    return J
  
def get_gradient(X, y, thetas, Lambda):
  m = y.size
  h = sigmoid(X.dot(thetas))
  zero_arr = np.array([0]).reshape(-1, 1)
  regularized_thetas = np.concatenate([zero_arr, thetas])
  grad = (1/m)*X.T.dot(h-y) + (Lambda/m)*regularized_thetas
  return grad.reshape(-1, 1)