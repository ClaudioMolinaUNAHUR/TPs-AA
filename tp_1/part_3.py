from utils.helpers import (
    accuracy_score,
    split_test_data,
    cargar_csv,
    confusion_matrix,
    recall_score,
    precision_score,
    f1_score,
    roc_curve,
)
from tp_1.addons.functions import (
    filter_data_prestamo,
)


def part_3():
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

    result = filter_data_prestamo(data, attrs, concepto, ages=[40, 45])

    test, train = split_test_data(result, test_size=0.3)

    evaluated = []
    # print(test[0])
    # discrete_naive_bayes(test[0], train, attrs, concepto, condicion_cumplida)
    # discrete_naive_bayes2(test[0], train, attrs, concepto, condicion_cumplida)
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
    print(tp, tn, fp, fn)
    accuracy = accuracy_score(tp, tn, fp, fn)
    recall = recall_score(tp, fn)
    precision = precision_score(tp, fp)
    f1 = f1_score(precision, recall)
    roc = roc_curve(evaluated, concepto, condicion_cumplida)
    return {
        "accuracy": accuracy,
        "f1": f1,
        "confusion_matrix": confusion_matrix_result,
        "roc": roc,
    }


def discrete_naive_bayes(test_row, train, attrs, concepto_column, condicion_cumplida):
    class_rows = {}
    N = len(train)
    pi = {}
    theta = {}
    laplace = 1
    num_vals_attr = {}

    for attr in attrs:
        value = test_row[attr]
        if value not in theta:
            theta[value] = {"attr": attr, "total": 0}

    for row in train:
        if row[concepto_column] not in class_rows:
            class_rows[row[concepto_column]] = []
            pi[row[concepto_column]] = 0

        class_rows[row[concepto_column]].append(row)
        
        for attr in attrs:
            value = row[attr]
            if attr not in num_vals_attr:
                num_vals_attr[attr] = set()
            num_vals_attr[attr].add(value)

        for value in theta:
            if value in row.values():
                theta[value]["total"] += 1
                theta[value][row[concepto_column]] = (
                    theta[value][row[concepto_column]] + 1
                    if row[concepto_column] in theta[value]
                    else 1
                )

    for classes in pi:
        # print(len(class_rows[classes]), classes, "total de registros de Cada")
        numerador = len(class_rows[classes]) + laplace
        denominador = N + laplace * len(class_rows)
        pi[classes] = numerador / denominador

    # print(pi, "% de cada")
    # print(theta)
    total_p = 0
    for classes in pi:
        producto = 1
        for value in theta:
            count = theta[value].get(classes, 0)
            numerador = count + laplace

            correccion_laplace = laplace * len(num_vals_attr[theta[value].get("attr")])
            N_register_class = len(class_rows[classes])

            denominador = N_register_class + correccion_laplace
            producto *= numerador / denominador

        # print(producto, classes, "PRODUCTO")
        pi[classes] *= producto
        total_p += pi[classes]
    # print(pi)
    accept = 0
    reject = 0
    for classes in pi:
        if classes == condicion_cumplida:
            accept = pi[classes] / total_p
        else:
            reject = pi[classes] / total_p

    # print(accept, reject)
    return accept if accept > reject else abs(reject - 1)


# TODO: poner print para el conj de prueba
