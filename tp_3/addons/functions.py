import math
import numpy as np
from sklearn.linear_model import LogisticRegression
import pandas as pd


def train_linear_regression_multiple(X, y):

    X_b = np.c_[np.ones((len(X), 1)), X]

    # Se obtiene traspuesta de X
    X_t = np.transpose(X_b)
    # producto de (X'X)
    X_t_X = np.dot(X_t, X_b)
    # Se calcula  inversa de (X'X)
    X_t_X_inversa = np.linalg.inv(X_t_X)
    # Formula previa (X'X)^-1X'
    X_t_X_i_multiplicado_X_t = np.dot(X_t_X_inversa, X_t)
    # Coeficiente de regresion (X'X)^-1X'y
    coefficient_reg = np.dot(X_t_X_i_multiplicado_X_t, y)
    return coefficient_reg


def predict_linear_regression(X, coefficient_reg):
    # Luego pasar el conj de entrenamiento con un for
    predict = []
    for row in X:
        sum = 0.0
        for i, B in enumerate(coefficient_reg):
            if i == 0:
                sum += B
            else:
                sum += row[i - 1] * B
        predict.append(sum)
    return predict


def r2_score(y_true, y_pred):
    # Promedio y
    sum = 0.0
    for value in y_true:
        sum += value[0]
    y_prom = sum / len(y_true)
    sst = 0.0
    for value in y_true:
        sst += (value[0] - y_prom) ** 2
    ssr = 0.0
    for value in y_pred:
        ssr += (value[0] - y_prom) ** 2

    return ssr / sst



def logistical_regresion(train, attrs, respuesta):
    #conversion a pandas DataFrame para usar sklearn
    pd_train = pd.DataFrame(train)
    
    # se separa X e y
    X_train = pd_train[attrs]
    y_train = pd_train[respuesta]
    
    # se instacia el modelo
    logreg = LogisticRegression(random_state=16)
    
    # se entrena el modelo
    logreg.fit(X_train, y_train)
    return logreg

def logistical_regresion_predict(log_reg, test, attrs, respuesta):
    df_test = pd.DataFrame(test)
    x_test_df = df_test[attrs]
    y_test_df = df_test[respuesta]
    y_pred_df = log_reg.predict(x_test_df)
    return y_pred_df, y_test_df
    