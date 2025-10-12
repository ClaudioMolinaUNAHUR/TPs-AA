# tp_3/part_1.py
from utils.helpers import cargar_csv, split_test_data, confusion_matrix
from tp_3.addons.functions import (
    train_linear_regression,
    predict_linear_regression,
    r2_score,
    train_logistic_regression,
    predict_logistic_regression,
    accuracy_score,
    recall_score,
    precision_score,
    f1_score,
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
    concepto_reg = "Calificación"
    concepto_cls = "Condición"
    condicion_cumplida = "Aprobado"
    prediction_column = "prediction"

    # 1) Split 80/20

    test, train = split_test_data(data, test_size=0.20)

    # ---------------- Regresión lineal (Calificación) ----------------
    X_train_reg = [[float(r[a]) for a in attrs] for r in train]
    y_train_reg = [float(r[concepto_reg]) for r in train]
    X_test_reg  = [[float(r[a]) for a in attrs] for r in test]
    y_test_reg  = [float(r[concepto_reg]) for r in test]

    theta = train_linear_regression(X_train_reg, y_train_reg)
    y_pred_reg = predict_linear_regression(X_test_reg, theta)
    y_pred_reg = np.asarray(y_pred_reg).ravel()  # asegurar forma (n,)
    r2 = r2_score(y_test_reg, y_pred_reg)


## Regresión logística (Condición)
    X_train_cls = [[float(r[a]) for a in attrs] for r in train]
    y_train_cls = [1 if r[concepto_cls] == condicion_cumplida else 0 for r in train]
    X_test_cls  = [[float(r[a]) for a in attrs] for r in test]
    y_test_cls  = [1 if r[concepto_cls] == condicion_cumplida else 0 for r in test]

    weights = train_logistic_regression(X_train_cls, y_train_cls, lr=0.001, epochs=5000)
    preds_cls, probs_cls = predict_logistic_regression(X_test_cls, weights, threshold=0.5)

    weights = train_logistic_regression(X_train_cls, y_train_cls, lr=0.001, epochs=5000)
    preds_cls, probs_cls = predict_logistic_regression(X_test_cls, weights, threshold=0.5)


    ####matriz

    predicted_rows = []
    for r, pred in zip(test, preds_cls):
        row = dict(r)
        row[prediction_column] = int(pred)
        predicted_rows.append(row)

    cm = confusion_matrix(predicted_rows, concepto_cls, prediction_column, condicion_cumplida)
    tp, tn, fp, fn = cm["tp"], cm["tn"], cm["fp"], cm["fn"]

    acc = accuracy_score(tp, tn, fp, fn)
    rec = recall_score(tp, fn)
    pre = precision_score(tp, fp)
    f1 = f1_score(pre, rec)