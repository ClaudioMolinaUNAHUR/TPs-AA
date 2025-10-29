# tp_3/part_1.py
import sys
import os

from sklearn import metrics

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.helpers import (
    cargar_csv,
    split_test_data,
    filter_data_estudiantes,
    accuracy_score,
    recall_score,
    precision_score,
    f1_score,
    confusion_matrix,
)
from tp_3.addons.functions import (
    train_linear_regression_multiple,
    predict_linear_regression,
    r2_score,
    logistical_regresion,
    logistical_regresion_predict,
)


def tp3_part_1():
    file_path = "./tp_3/Estudiantes.csv"
    data = cargar_csv(file_path, "latin-1")

    attrs = [
        "Horas de estudio por semana",
        "Calificaciones previas",
        "Porcentaje de asistencia",
    ]

    #------- REGRESION LINEAL-------#
    respuesta = "Calificación"
    
    
    result = filter_data_estudiantes(data, attrs, respuesta)
    test, train = split_test_data(result, test_size=0.20)

    X_test_reg = []
    y_test_reg = []

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

    ## se usa "y" para regresion multiple, con valores continuos
    coefficient_reg = train_linear_regression_multiple(X_train_reg, y_train_reg)
    y_pred_reg = predict_linear_regression(X_test_reg, coefficient_reg)
    
    #------- REGRESION LINEAL METRICAS-------#
    r2 = r2_score(y_test_reg, y_pred_reg)


    #------- REGRESION LOGISTICA -------#
    respuesta_log_reg = "Condición"
    condicion_cumplida = "Aprobado"
    prediction_column = "prediction"
    
    ## se usa "y" para regresion logistica, con valores categoricos
    result_log_reg = filter_data_estudiantes(
        data, attrs, respuesta_log_reg, classification=True
    )
    test_log_reg, train_log_reg = split_test_data(result_log_reg, test_size=0.20)
    LogRegression = logistical_regresion(train_log_reg, attrs, respuesta_log_reg)

    y_pred_df = logistical_regresion_predict(
        LogRegression, test_log_reg, attrs
    )
    
    predicted = []
    for i, row in enumerate(test_log_reg):
        row[prediction_column] = 1 if condicion_cumplida == y_pred_df[i] else 0
        predicted.append(row)
        
    #------- REGRESION LOGISTICA METRICAS-------#
    confusion_matrix_result, matrix, str_matrix = confusion_matrix(
        predicted, respuesta_log_reg, prediction_column, condicion_cumplida
    )

    tp = confusion_matrix_result["tp"]
    tn = confusion_matrix_result["tn"]
    fp = confusion_matrix_result["fp"]
    fn = confusion_matrix_result["fn"]

    accuracy = accuracy_score(tp, tn, fp, fn)
    recall = recall_score(tp, fn)
    precision = precision_score(tp, fp)
    f1 = f1_score(precision, recall)

    #------- Nuevo estudiante a predecir -------
    test_new_student = {attrs[0]: 25.0, attrs[1]: 0.58, attrs[2]: 68.0}
    
    test_student = []
    for attr in attrs:
        test_student.append(test_new_student[attr])
    y_pred_test_student_linear = predict_linear_regression(
        [test_student], coefficient_reg
    )
    y_pred_test_student_logistic = logistical_regresion_predict(
        LogRegression, [test_new_student], attrs
    )
    
    return {
        "split": {"train": len(train), "test": len(test), "proporcion_test": 0.20},
        "attrs": attrs,
        "respuesta": respuesta,
        "regresion_lineal": {
            "student_pred": y_pred_test_student_linear,
            "coefficient_reg": coefficient_reg,
            "r2_test": r2,
        },
        "respuesta_log_reg": respuesta_log_reg,
        "regresion_logistica": {
            "student_pred": y_pred_test_student_logistic[0],
            "coefficient_reg": LogRegression.coef_,
            "B0": LogRegression.intercept_,
            "accuracy": accuracy,
            "matrix": str_matrix,
            "confusion_matrix": {"tp": tp, "tn": tn, "fp": fp, "fn": fn},
            "f1": f1,
        },
    }
