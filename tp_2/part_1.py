from utils.helpers import (
    cargar_csv,
    split_test_data,
    confusion_matrix,
    f1_score,
    precision_score,
    accuracy_score,
    recall_score,
    filter_data_prestamo,
    save_json
)
from tp_2.addons.functions import id3, evaluate_id3

def tp2_part_1():
    file_path = "./tp_1/Préstamo.csv"
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
    tree = id3(train, attrs, concepto)
    # print(tree)
    evaluated = []
    print("test: ", len(test))
    print("train: ", len(train))
    print("total: ", len(result))
    for row in test:
        clase = evaluate_id3(row, tree)
        row[prediction_column] = 1 if condicion_cumplida == clase else 0
        evaluated.append(row)

    confusion_matrix_result = confusion_matrix(
        evaluated, concepto, prediction_column, condicion_cumplida
    )

    tp = confusion_matrix_result["tp"]
    tn = confusion_matrix_result["tn"]
    fp = confusion_matrix_result["fp"]
    fn = confusion_matrix_result["fn"]

    accuracy = accuracy_score(tp, tn, fp, fn)
    recall = recall_score(tp, fn)
    precision = precision_score(tp, fp)
    f1 = f1_score(precision, recall)
    save_json("./tp_2/tree.json", tree)
    return {
        "accuracy": accuracy,
        "f1": f1,
        "confusion_matrix": confusion_matrix_result,
    }