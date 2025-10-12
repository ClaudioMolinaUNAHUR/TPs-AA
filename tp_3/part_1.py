# tp_3/part_1.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.helpers import (
    cargar_csv,
    split_test_data,
    filter_data_estudiantes,
    confusion_matrix,
    accuracy_score,
    recall_score,
    precision_score,
    f1_score,
)
from tp_3.addons.functions import (
    train_linear_regression,
    predict_linear_regression,
    r2_score,
    train_logistic_regression,
    predict_logistic_regression,
)
import numpy as np


def tp3_part_1():
    file_path = "./tp_3/Estudiantes.csv"
    data = cargar_csv(file_path, "latin-1")

    attrs = [
        "Horas de estudio por semana",
        "Calificaciones previas",
        "Porcentaje de asistencia",
    ]
    respuesta = "Calificación"

    result = filter_data_estudiantes(data, attrs, respuesta)
    test, train = split_test_data(result, test_size=0.20)

    X_test_reg  = []
    y_test_reg  = []
    
    for row in test:
       row_predictoria = [row[a] for a in attrs]
       X_test_reg.append(row_predictoria)
       y_test_reg.append([row[respuesta]])
        
    X_train_reg = []
    y_train_reg = []
    
    for row in train:
        row_predictoria = [row[a] for a in attrs]
        X_train_reg.append(row_predictoria)
        y_train_reg.append([row[respuesta]])

        
    print('test', X_test_reg)
    print('test', y_test_reg)

    coefficient_reg = train_linear_regression(X_train_reg, y_train_reg)
    y_pred_reg = predict_linear_regression(X_test_reg, coefficient_reg)
    r2 = r2_score(y_test_reg, y_pred_reg)
    
    
    t = np.asarray(coefficient_reg).ravel().tolist()
    ecuacion = {
        "intercepto": float(t[0]),
        attrs[0]: float(t[1]),
        attrs[1]: float(t[2]),
        attrs[2]: float(t[3]),
    }

    return {
        "split": {"train": len(train), "test": len(test), "proporcion_test": 0.20},
        "regresion_lineal": {
            "features": attrs,
            "ecuacion": ecuacion, 
            "r2_test": r2,
        },
    }




# ## Regresión logística (Condición)
#     X_train_cls = [[float(r[a]) for a in attrs] for r in train]
#     y_train_cls = [1 if r[concepto_cls] == condicion_cumplida else 0 for r in train]
#     X_test_cls  = [[float(r[a]) for a in attrs] for r in test]
#     y_test_cls  = [1 if r[concepto_cls] == condicion_cumplida else 0 for r in test]

#     weights = train_logistic_regression(X_train_cls, y_train_cls, lr=0.001, epochs=5000)
#     preds_cls, probs_cls = predict_logistic_regression(X_test_cls, weights, threshold=0.5)

#     weights = train_logistic_regression(X_train_cls, y_train_cls, lr=0.001, epochs=5000)
#     preds_cls, probs_cls = predict_logistic_regression(X_test_cls, weights, threshold=0.5)


    ####matriz

    # predicted_rows = []
    # for r, pred in zip(test, preds_cls):
    #     row = dict(r)
    #     row[prediction_column] = int(pred)
    #     predicted_rows.append(row)

    # cm = confusion_matrix(predicted_rows, concepto_cls, prediction_column, condicion_cumplida)
    # tp, tn, fp, fn = cm["tp"], cm["tn"], cm["fp"], cm["fn"]

    # acc = accuracy_score(tp, tn, fp, fn)
    # rec = recall_score(tp, fn)
    # pre = precision_score(tp, fp)
    # f1 = f1_score(pre, rec)