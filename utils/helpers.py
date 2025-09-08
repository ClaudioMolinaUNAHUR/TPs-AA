import numpy as np
import csv
import math
import matplotlib.pyplot as plt


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

    auc = np.trapezoid(TPR_array, FPR_array)
    return {
        "auc": auc,
        "tpr": TPR_array,
        "fpr": FPR_array
    }


def plot_roc_curve(fpr, tpr, auc, title="Curva ROC", save_path=None):
    """
    Grafica la curva ROC
    
    Args:
        fpr: Array de tasas de falsos positivos
        tpr: Array de tasas de verdaderos positivos  
        auc: Área bajo la curva
        title: Título del gráfico
        save_path: Ruta para guardar el gráfico (opcional)
    """
    plt.figure(figsize=(8, 6))
    
    # Graficar la curva ROC
    plt.plot(fpr, tpr, color='darkorange', lw=2, 
             label=f'Curva ROC (AUC = {auc:.3f})')
    
    # Graficar la línea diagonal (clasificador aleatorio)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', 
             label='Clasificador aleatorio')
    
    # Configurar el gráfico
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('Tasa de Falsos Positivos (FPR)')
    plt.ylabel('Tasa de Verdaderos Positivos (TPR)')
    plt.title(title)
    plt.legend(loc="lower right")
    plt.grid(True, alpha=0.3)
    
    # Guardar si se especifica una ruta
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Gráfico guardado en: {save_path}")
    
    plt.show()


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
