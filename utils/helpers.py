import csv
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline


def accuracy_score(tp, tn, fp, fn):
    # marca la deteccion de positivos, pero no negativos
    correct = tp + tn
    total = tp + tn + fp + fn
    return correct / total


def specificity_score(tn, fp):
    # probabilidad de detectar un neg
    return tn / (tn + fp) if tn + fp != 0 else 0


def recall_score(tp, fn):
    # probabilidad de detectar un pos
    return tp / (tp + fn) if fn + tp != 0 else 0


def precision_score(tp, fp):
    # probabilidad de detectar correctamente casos pos
    return tp / (tp + fp) if fp + tp != 0 else 0


def balanced_accuracy_score(recall, specificity):
    # similar a accuracy pero con clases desbalanceadas
    return (recall + specificity) / 2


def f1_score(precision, recall):
    # medida de calidad mas general
    return (
        2 * precision * recall / (precision + recall) if precision + recall != 0 else 0
    )


def TPR_score(tp, fn):
    # tasa verdaderos positivos
    return recall_score(tp, fn)


def FPR_score(fp, tn):
    # tasa falsos positivos
    return fp / (fp + tn) if tn + fp != 0 else 0


def complement_specificity_score(specificity):
    return 1 - specificity


def umbral_equal(recall_array, specificity_array):
    return np.argmin(np.abs(recall_array - specificity_array))


def umbral_youden(recall_array, specificity_array):
    return np.argmax(recall_array + specificity_array - 1)


def umbral_closer_point(recall_array, specificity_array):
    return np.argmin(recall_array**2 + (specificity_array - 1) ** 2)


data = [
    {"name": "A", "score": 0.98, "cl": 1},
    {"name": "B", "score": 0.83, "cl": 1},
    {"name": "C", "score": 0.75, "cl": 0},
    {"name": "D", "score": 0.69, "cl": 1},
    {"name": "E", "score": 0.63, "cl": 1},
    {"name": "F", "score": 0.52, "cl": 0},
    {"name": "G", "score": 0.45, "cl": 0},
    {"name": "H", "score": 0.38, "cl": 0},
    {"name": "I", "score": 0.22, "cl": 0},
    {"name": "J", "score": 0.1, "cl": 0},
]


def roc_curve(data, key_class, condicion_cumplida):
    TPR_array = []
    FPR_array = []
    length = len(data)
    for umbral in range(length):
        tp = 0
        tn = 0
        fp = 0
        fn = 0
        for index, item in enumerate(data):
            if umbral <= index:
                if item[key_class] == condicion_cumplida:
                    fn += 1
                else:
                    tn += 1
            else:
                if item[key_class] == condicion_cumplida:
                    tp += 1
                else:
                    fp += 1
        TPR = TPR_score(tp, fn)
        FPR = FPR_score(fp, tn)
        TPR_array.append(TPR)
        FPR_array.append(FPR)
    
    # PLOT HACIENDO SUAVIZADO DE CURVA
    x = np.array(FPR_array) 
    y = np.array(TPR_array) 
    print("x:", x,"y:", y)
    # Ordenar por x
    order = np.argsort(x)
    x = x[order]
    y = y[order]

    x, idx = np.unique(x, return_index=True)
    y = y[idx]

    x_new = np.linspace(x.min(), x.max(), 500)
    f = make_interp_spline(x, y, k=2)  # cuadrática
    y_smooth = f(x_new)
    plt.plot (x_new,y_smooth)
    plt.scatter (x, y)
    plt.show()

    return np.trapezoid(TPR_array, FPR_array)


def cargar_csv(file_path, encoding="utf-8"):
    try:
        data = []
        with open(file_path, "r", encoding=encoding) as file:
            csv_reader = csv.DictReader(file)
            data = [row for row in csv_reader]
        return data
    except Exception as e:
        print(f"Error al leer el CSV: {e}")
        return []


def split_test_data(data, test_size=0.2):
    length = len(data)
    parts = math.floor(length * test_size)
    set_length = length // parts - 1
    test, train = [], []
    pos_to_take = 0
    mod = length % parts

    for i in range(parts):
        start = length // parts * i if i != 0 else 0
        end = length // parts * (i + 1)

        if end > length:
            end = length
        # start y end van cambiando el orden en el cual eligen en cada iteracion un dato para test
        set_data = data[start:end]

        # verifica que la posicion no sea mayor al largo del set
        if pos_to_take >= set_length:
            pos_to_take = 0
        value = set_data.pop(pos_to_take)

        test.append(value)
        train.extend(set_data)

        # caso donde tengo resto
        if i + 1 == parts and mod != 0:
            set_data = data[end:length]
            if pos_to_take > len(set_data):
                pos_to_take = 0
            value = set_data.pop(pos_to_take)
            test.append(value)
            train.extend(set_data)
        pos_to_take += 1

    return test, train


def confusion_matrix(data, concepto, prediction_column, condicion_cumplida):
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for row in data:
        if row[concepto] == condicion_cumplida:
            if row[prediction_column] > 0.5:
                tp += 1
            else:
                fn += 1
        else:
            if row[prediction_column] > 0.5:
                fp += 1
            else:
                tn += 1
    return {"tp": tp, "tn": tn, "fp": fp, "fn": fn}
