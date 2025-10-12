
import math
import numpy as np


def train_linear_regression(X, y):

  X_b = np.c_[np.ones((len(X), 1)), X]

  #Se obtiene traspuesta de X
  X_t = np.transpose(X_b)
  #producto de (X'X)
  X_t_X = np.dot(X_t,X_b)
   #Se calcula  inversa de (X'X)
  X_t_X_inversa = np.linalg.inv(X_t_X)
  #Formula previa (X'X)^-1X'
  X_t_X_i_multiplicado_X_t = np.dot(X_t_X_inversa,X_t)
  #Coeficiente de regresion (X'X)^-1X'y
  coefficient_reg = np.dot(X_t_X_i_multiplicado_X_t,y)
  return ( 
    coefficient_reg
    )


  

def predict_linear_regression(X, theta):
    X = np.asarray(X, dtype=float)
    X_b = np.c_[np.ones((len(X), 1)), X]
    y_hat = X_b @ theta
    return y_hat

def r2_score(y_true, y_pred):
    y_true = np.asarray(y_true, dtype=float).ravel()
    y_pred = np.asarray(y_pred, dtype=float).ravel()
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1.0 - ss_res / ss_tot if ss_tot != 0 else 0.0




# ----------------------------
#  TODO:  REGRESIÓN LOGÍSTICA
# ----------------------------
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def train_logistic_regression(X, y, lr=0.001, epochs=10000):

    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float).reshape(-1, 1)

    n, m = X.shape
    X_b = np.c_[np.ones((n, 1)), X]
    weights = np.zeros((m + 1, 1))

    for _ in range(epochs):
        z = X_b @ weights
        h = sigmoid(z)
        gradient = (X_b.T @ (h - y)) / n
        weights -= lr * gradient

    return weights

def predict_logistic_regression(X, weights, threshold=0.5):
    X = np.array(X, dtype=float)
    X_b = np.c_[np.ones((len(X), 1)), X]
    proba = sigmoid(X_b @ weights)
    preds = (proba >= threshold).astype(int)
    return preds, proba

# ----------------------------
#   MÉTRICAS
# ----------------------------
