from utils.helpers import (
    cargar_csv,
    split_test_data,
    confusion_matrix,
    f1_score,
    precision_score,
    accuracy_score,
    recall_score,
    filter_data_prestamo,
    save_json,
)
from tp_2.addons.functions import discrete_id3, predict_id3


def tp2_part_1():
    file_path = "./tp_1/Préstamo.csv"
    file_path_tree = "./tp_2/results/tree.json"
    data = cargar_csv(file_path, "latin-1")

    attrs = [
        "Sexo",
        "Mayor nivel educativo",
        "Estado de vivienda",
        "Préstamos previos impagos",
        "Destino de los fondos",
    ]
    concepto = "Estado"
    condicion_cumplida = "OTORGADO"
    prediction_column = "prediction"

    result = filter_data_prestamo(data, attrs, concepto, ages=[40, 45], between=True)
    test, train = split_test_data(result, test_size=0.20)

    _, tree = discrete_id3(train, attrs, concepto)
    save_json(file_path_tree, tree)

    predicted = []
    for row in test:
        clase = predict_id3(row, tree)
        row[prediction_column] = 1 if condicion_cumplida == clase else 0
        predicted.append(row)

    confusion_matrix_result, matrix, str_matrix = confusion_matrix(
        predicted, concepto, prediction_column, condicion_cumplida
    )

    tp = confusion_matrix_result["tp"]
    tn = confusion_matrix_result["tn"]
    fp = confusion_matrix_result["fp"]
    fn = confusion_matrix_result["fn"]

    accuracy = accuracy_score(tp, tn, fp, fn)
    recall = recall_score(tp, fn)
    precision = precision_score(tp, fp)
    f1 = f1_score(precision, recall)
    return {
        "accuracy": accuracy,
        "f1": f1,
        "confusion_matrix": str_matrix,
    }
