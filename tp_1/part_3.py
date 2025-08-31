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
    types_vals_attr = {}

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
            value_row = row[attr]
            if attr not in types_vals_attr:
                types_vals_attr[attr] = set()
            types_vals_attr[attr].add(value_row)

            for value_t in theta:
                if value_t == value_row and theta[value_t]["attr"] == attr:
                    theta[value_t]["total"] += 1
                    theta[value_t][row[concepto_column]] = (
                        theta[value_t][row[concepto_column]] + 1
                        if row[concepto_column] in theta[value_t]
                        else 1
                    )
                    break

    for K in pi:
        # print(len(class_rows[classes]), classes, "total de registros de Cada")
        total_items_in_class = len(class_rows[K])
        numerador = total_items_in_class + laplace
        
        total_Ks = len(class_rows)
        denominador = N + laplace * total_Ks
        
        pi[K] = numerador / denominador

    # print(pi, "% de cada")
    # print(theta)
    total_probability = 0
    probability = {}
    for K in pi:
        producto = 1
        for value in theta:
            count = theta[value].get(K, 0)
            numerador = count + laplace

            quantity_values_from_attr = len(types_vals_attr[theta[value].get("attr")])
            N_register_class = len(class_rows[K])

            denominador = N_register_class + laplace * quantity_values_from_attr

            producto *= numerador / denominador

        # print(producto, classes, "PRODUCTO")
        probability[K] = pi[K] * producto
        total_probability += probability[K]
    # print(pi)
    accept = 0
    reject = 0
    for K in probability:
        if K == condicion_cumplida:
            accept = probability[K] / total_probability
        else:
            reject = probability[K] / total_probability

    # print(accept, reject)
    return accept if accept > reject else abs(reject - 1)


# TODO: poner print para el conj de prueba
