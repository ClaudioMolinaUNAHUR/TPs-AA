import numpy as np
from utils.helpers import (
    accuracy_score,
    split_test_data,
    cargar_csv,
    confusion_matrix,
    specificity_score,
    recall_score,
    precision_score,
    f1_score,
    TPR_score,
    FPR_score,
    filter_data_prestamo,
)
from tp_1.addons.functions import (
    get_hipotesis_find_s,
    predict_find_s,
)


def part_1_2():
    file_path = "./tp_1/Préstamo.csv"
    data = cargar_csv(file_path, "latin-1")

    attrs = [
        "Sexo",
        "Mayor nivel educativo",
        "Estado de vivienda",
        "Préstamos previos impagos",
    ]
    concepto = "Estado"
    condicion_cumplida = "OTORGADO"
    prediction_column = "prediction"

    result = filter_data_prestamo(data, attrs, concepto, ages=[50])

    test, train = split_test_data(result, test_size=0.25)
    hipotesis = get_hipotesis_find_s(train, attrs, concepto, condicion_cumplida)

    predicted = predict_find_s(test, hipotesis, attrs, prediction_column)
    confusion_matrix_result = confusion_matrix(
        predicted, concepto, prediction_column, condicion_cumplida
    )

    tp = confusion_matrix_result["tp"]
    tn = confusion_matrix_result["tn"]
    fp = confusion_matrix_result["fp"]
    fn = confusion_matrix_result["fn"]
    
    accuracy = accuracy_score(tp, tn, fp, fn)
    specificity = specificity_score(tn, fp)
    recall = recall_score(tp, fn)
    precision = precision_score(tp, fp)
    f1 = f1_score(precision, recall)
    TPR = TPR_score(tp, fn)
    FPR = FPR_score(fp, tn)

    return {
        "hipotesis": hipotesis,
        "accuracy": accuracy,
        "specificity": specificity,
        "recall": recall,
        "precision": precision,
        "f1": f1,
        "TPR": TPR,
        "FPR": FPR,
        "confusion_matrix": confusion_matrix_result,
    }


# TODO: poner print para el conj de prueba
