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
    # (Si tu helper acepta random_state, podés pasarlo para reproducibilidad.)
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