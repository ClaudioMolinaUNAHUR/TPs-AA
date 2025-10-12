from utils.helpers import (
    cargar_csv,
    split_test_data,
    confusion_matrix,
    f1_score,
    precision_score,
    accuracy_score,
    recall_score,
    save_json,
)


def tp3_part_1():
    file_path = "./tp_3/Estudiantes.csv"
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

    test, train = split_test_data(data, test_size=0.20)

    # confusion_matrix_result = confusion_matrix(
    #     predicted, concepto, prediction_column, condicion_cumplida
    # )

    # tp = confusion_matrix_result["tp"]
    # tn = confusion_matrix_result["tn"]
    # fp = confusion_matrix_result["fp"]
    # fn = confusion_matrix_result["fn"]

    # accuracy = accuracy_score(tp, tn, fp, fn)
    # recall = recall_score(tp, fn)
    # precision = precision_score(tp, fp)
    # f1 = f1_score(precision, recall)
    # return {
    #     "accuracy": accuracy,
    #     "f1": f1,
    #     "confusion_matrix": confusion_matrix_result,
    # }