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
)
from tp_1.addons.functions import (
    filter_data_prestamo,
    get_hipotesis_find_s,
    evaluate_find_s,
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
    #print(test[0])
    # discrete_naive_bayes(test[0], train, attrs, concepto, condicion_cumplida)
    for row in test:
        result = discrete_naive_bayes(row, train, attrs, concepto, condicion_cumplida)
        row[prediction_column] = result
        evaluated.append(row)
       
    print(evaluated)
    # confusion_matrix_result = confusion_matrix(
    #     evaluated, concepto, prediction_column, condicion_cumplida
    # )

    # 1 - pi - cantidad de una clase  / cantidad de casos totales
    # 2 - Theta - se toma 1 estado categorico de 1 atributo y ademas que esten con en clase, y luego en la otra
    # 3 - se multiplica pi * productoria de todos los theta de esa clase
    # tp = confusion_matrix_result["tp"]
    # tn = confusion_matrix_result["tn"]
    # fp = confusion_matrix_result["fp"]
    # fn = confusion_matrix_result["fn"]
    # accuracy = accuracy_score(tp, tn, fp, fn)
    # specificity = specificity_score(tn, fp)
    # recall = recall_score(tp, fn)
    # precision = precision_score(tp, fp)
    # f1 = f1_score(precision, recall)
    # TPR = TPR_score(tp, fn)
    # FPR = FPR_score(fp, tn)
    # return {
    #     "accuracy": accuracy,
    #     "specificity": specificity,
    #     "recall": recall,
    #     "precision": precision,
    #     "f1": f1,
    #     "TPR": TPR,
    #     "FPR": FPR,
    #     "confusion_matrix": confusion_matrix_result,
    # }


def discrete_naive_bayes(test_row, train, attrs, concepto_column, condicion_cumplida):
    classFinded = {}
    length = len(train)
    pi = {}
    theta = {}
    laplace = 1
    for attr in attrs:
        value = test_row[attr]
        if value not in theta:
            theta[value] = {"total": 0}
    print(theta)
    for row in train:
        if row[concepto_column] not in classFinded:
            classFinded[row[concepto_column]] = []
            pi[row[concepto_column]] = 0

        classFinded[row[concepto_column]].append(row)

        for value in theta:
            if value in row.values():
                theta[value]["total"] += 1
                theta[value][row[concepto_column]] = (
                    theta[value][row[concepto_column]] + 1
                    if row[concepto_column] in theta[value]
                    else 1
                )
    
    for classes in pi:
        print(len(classFinded[classes]), classes, "total de registros de Cada")
        pi[classes] = (len(classFinded[classes]) + laplace) / (length + laplace * len(classFinded))
    print(pi, "% de cada")
    print(theta)
    total_p = 0
    for classes in pi:
        producto = 1
        for value in theta:            
            count = theta[value].get(classes, 0)
            print(classes , (count + laplace) / (theta[value]["total"] + laplace * len(classFinded)), value, "COUNT")
            producto *= (count + laplace) / (theta[value]["total"] + laplace * len(classFinded))
        print(producto, classes, "PRODUCTO")
        pi[classes] *= producto
        total_p += pi[classes]
    print(pi)
    accept = 0
    reject = 0
    for classes in pi:
        if classes == condicion_cumplida:
            accept = pi[classes] / total_p
        else:
            reject = pi[classes] / total_p
            
    print(accept, reject)
    return accept if accept > reject else abs(reject - 1)


# TODO: poner print para el conj de prueba
