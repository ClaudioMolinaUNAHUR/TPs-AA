# tp_3/addons/functions.py
import math
import numpy as np

# ----------------------------
#   REGRESIÓN LINEAL MÚLTIPLE
# ----------------------------
def train_linear_regression(X, y):
  
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float).reshape(-1, 1)

    # Agregamos columna de 1s para el término independiente
    X_b = np.c_[np.ones((len(X), 1)), X]

    # Ecuación normal: (XᵀX)⁻¹Xᵀy
    theta = np.linalg.pinv(X_b.T @ X_b) @ X_b.T @ y
    return theta  # incluye intercepto en la primera posición

def predict_linear_regression(X, theta):
    X = np.array(X, dtype=float)
    X_b = np.c_[np.ones((len(X), 1)), X]
    return X_b @ theta

def r2_score(y_true, y_pred):
    y_true = np.array(y_true, dtype=float)
    y_pred = np.array(y_pred, dtype=float)
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - ss_res / ss_tot


# ----------------------------
#   REGRESIÓN LOGÍSTICA
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
