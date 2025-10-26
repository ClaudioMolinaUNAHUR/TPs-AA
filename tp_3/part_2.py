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
from tp_3.addons.functions import search_svm


def tp3_part_2():
    file_path = "./tp_3/Estudiantes.csv"
    data = cargar_csv(file_path, "latin-1")

    attrs = [
        "Horas de estudio por semana",
        "Calificaciones previas",
        "Porcentaje de asistencia",
    ]
    respuesta = "Condición"
    condicion_cumplida = "Aprobado"
    prediction_column = "prediction"

    ## se usa "y" para regresion logistica, con valores categoricos
    result = filter_data_estudiantes(data, attrs, respuesta, classification=True)
    test, train = split_test_data(result, test_size=0.20)

    C_values = [0.01, 0.1, 1, 10, 100]
    gamma_values = [10, 1, 0.1, 0.01]
    r_values = [-1.0, -0.5, 0.0, 0.5, 1.0]
    kernels = ["rbf", "linear", "sigmoid", "poly"]

    results_kernel_score = []

    for kernel_type in kernels:
        results = search_svm(
            train,
            test,
            attrs,
            respuesta,
            kernel=kernel_type,
            C_values=C_values,
            r_values=r_values,
            gamma_values=gamma_values,
            prediction_column=prediction_column,
            condicion_cumplida=condicion_cumplida,
        )
        svm_score = []
        for predicted in results:
            confusion_matrix_result = confusion_matrix(
                predicted["predicted"], respuesta, prediction_column, condicion_cumplida
            )
            tp = confusion_matrix_result["tp"]
            tn = confusion_matrix_result["tn"]
            fp = confusion_matrix_result["fp"]
            fn = confusion_matrix_result["fn"]

            accuracy = accuracy_score(tp, tn, fp, fn)
            recall = recall_score(tp, fn)
            precision = precision_score(tp, fp)
            f1 = f1_score(precision, recall)
            
            predicted.pop("predicted")
            svm_score.append(
                {
                    **predicted,
                    "accuracy": accuracy,
                    "confusion_matrix": {"tp": tp, "tn": tn, "fp": fp, "fn": fn},
                    "f1": f1,
                }
            )
        best_result = max(svm_score, key=lambda x: x["accuracy"])
        results_kernel_score.append({"kernel": kernel_type, "best_result": best_result})

    print(results_kernel_score)

    # #------- Nuevo estudiante a predecir -------
    # test_new_student = {attrs[0]: 25.0, attrs[1]: 0.58, attrs[2]: 68.0}

    # test_student = []
    # y_pred_test_student_logistic = logistical_regresion_predict(
    #     LogRegression, [test_new_student], attrs
    # )

    # return {
    #     "split": {"train": len(train), "test": len(test), "proporcion_test": 0.20},
    #     "respuesta_log_reg": respuesta,
    #     "regresion_logistica": {
    #         "ecuacion": y_pred_test_student_logistic[0],
    #         "coefficient_reg": LogRegression.coef_,
    #         "B0": LogRegression.intercept_,
    #         "accuracy": accuracy,
    #         "confusion_matrix": {"tp": tp, "tn": tn, "fp": fp, "fn": fn},
    #         "f1": f1,
    #     },
    # }
