import numpy as np
from collections import defaultdict, Counter


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
    discrete_naive_bayes(test[0], train, attrs, concepto, condicion_cumplida)
    #for row in test:
     #   result = discrete_naive_bayes(row, train, attrs, concepto, condicion_cumplida)
      #  row[prediction_column] = result
       # evaluated.append(row)
       
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
    """
    Versión binaria (2 clases) de Naive Bayes categórico con Laplace.
    - attrs: lista de columnas categóricas
    - concepto_column: nombre de la columna de clase
    - condicion_cumplida: etiqueta de la clase "positiva" que querés medir (p.ej. 'Sí')
    Devuelve: probabilidad P(Y=condicion_cumplida | x)
    """
    laplace = 1.0

    # ---- 1) Priors P(Y=c) con Laplace ----
    class_counts = Counter(row[concepto_column] for row in train)
  
    classes = list(class_counts.keys())
    if len(classes) != 2:
        raise ValueError("Esta función asume exactamente 2 clases.")
    N = len(train); K = 2

    pi = {c: (class_counts[c] + laplace) / (N + laplace * K) for c in classes}

    # Para normalizar por clase en cada atributo (denominador), guardo filas por clase
    class_rows = {c: [] for c in classes}
    for row in train:
        class_rows[row[concepto_column]].append(row)

    # ---- 2) Vocabularios por atributo (|V_attr|) ----
    vocab = {a: set(r[a] for r in train) for a in attrs}
    for a in attrs:
        vocab[a].add(test_row[a])  # por si en test aparece valor no visto

    # ---- 3) Conteos por atributo/valor/clase: counts[attr][valor][clase] ----
    counts = {a: defaultdict(Counter) for a in attrs}
    for r in train:
        c = r[concepto_column]
        for a in attrs:
            v = r[a]
            counts[a][v][c] += 1

    # ---- 4) Producto de likelihoods por clase ----
    unnormalized = {}
    for c in classes:
        producto = 1.0
        class_n = len(class_rows[c])
        for a in attrs:
            v = test_row[a]
            Va = len(vocab[a])                            # |V_attr|
            num = counts[a][v][c] + laplace              # conteo del valor en esa clase + α
            den = class_n + laplace * Va                 # total de esa clase + α*|V_attr|
            producto *= (num / den)
        unnormalized[c] = pi[c] * producto

    # ---- 5) Normalización a posteriors ----
    Z = sum(unnormalized.values())
    post = {c: (unnormalized[c] / Z) if Z > 0 else 0.5 for c in classes}

    accept = post.get(condicion_cumplida, 0.0)
    reject = 1.0 - accept

    # (prints de depuración, opcionales)
    # print("pi:", pi)
    # print("post:", post)
    # print("accept, reject:", accept, reject)

    # Devolver como antes: prob de la clase pedida
    return accept

# TODO: poner print para el conj de prueba
