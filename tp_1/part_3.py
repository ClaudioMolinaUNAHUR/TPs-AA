from utils.helpers import (
    accuracy_score,
    split_test_data,
    cargar_csv,
    confusion_matrix,
    recall_score,
    precision_score,
    f1_score,
    roc_curve,
    filter_data_prestamo,
)
from tp_1.addons.functions import discrete_naive_bayes


def part_3():
    file_path = "./tp_1/Préstamo.csv"
    file_path_roc = "./tp_1/roc_curve.png"
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

    result = filter_data_prestamo(data, attrs, concepto, ages=[40, 45])

    test, train = split_test_data(result, test_size=0.2)

    evaluated = []
    # print(test[0])
    # discrete_naive_bayes(test[0], train, attrs, concepto, condicion_cumplida)
    for row in test:
        result = discrete_naive_bayes(row, train, attrs, concepto, condicion_cumplida)
        row[prediction_column] = result
        evaluated.append(row)

    confusion_matrix_result = confusion_matrix(
        evaluated, concepto, prediction_column, condicion_cumplida
    )

    # 1 - pi - cantidad de una clase  / cantidad de casos totales
    # 2 - Theta - se toma 1 estado categorico de 1 atributo y ademas que esten con en clase, y luego en la otra
    # 3 - se multiplica pi * productoria de todos los theta de esa clase
    tp = confusion_matrix_result["tp"]
    tn = confusion_matrix_result["tn"]
    fp = confusion_matrix_result["fp"]
    fn = confusion_matrix_result["fn"]
    
    accuracy = accuracy_score(tp, tn, fp, fn)
    recall = recall_score(tp, fn)
    precision = precision_score(tp, fp)
    f1 = f1_score(precision, recall)
    auc = roc_curve(evaluated, concepto, condicion_cumplida, file_path_roc)
    return {
        "accuracy": accuracy,
        "f1": f1,
        "confusion_matrix": confusion_matrix_result,
        "auc": auc,
    }


# TODO: poner print para el conj de prueba
