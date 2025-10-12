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


    test, train = split_test_data(data, test_size=0.20)

  