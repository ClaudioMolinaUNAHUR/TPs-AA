import sys
import os
from utils.helpers import (
    cargar_csv,
    split_test_data,
    filter_data_wines,
    confusion_matrix_multiclase,
    calculate_metrics,
)
from tp_4.addons.functions import (
    knn_mean,
    standarize_data,
    predict_kmeans,
)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def tp4_part_2():
    file_path = "./tp_4/winequality-red.csv"
    data = cargar_csv(file_path, "latin-1", delimiter=";")

    attrs = [
        "fixed acidity",
        "volatile acidity",
        "citric acid",
        "residual sugar",
        "chlorides",
        "free sulfur dioxide",
        "total sulfur dioxide",
        "density",
        "pH",
        "sulphates",
        "alcohol",
    ]

    respuesta = "quality"
    prediction_column = "prediction"

    result = filter_data_wines(data, attrs, respuesta)
    test, train = split_test_data(result, test_size=0.20)

    train_std = standarize_data(train, attrs)
    test_std = standarize_data(test, attrs)

    Ks = [2, 3, 4, 5]

    for K in Ks:
        clusters = knn_mean(train_std, attrs, K)
        for row in test_std:
            # Asegurás que prediction_column sea un dict
            row[prediction_column] = row.get(prediction_column, {})

            # Luego usás setdefault para asignar si no existe esa clave K
            row[prediction_column].setdefault(
                K, predict_kmeans(train_std, row, attrs, respuesta, clusters)
            )

    confusion_matrix = {}
    knn_metrics = {}
    for K in Ks:
        preds = []
        for row in test_std:
            # Crear una copia mínima del registro, cambiando solo la predicción
            new_row = row.copy()
            new_row[prediction_column] = row[prediction_column][K]
            preds.append(new_row)

        confusion_matrix[K] = confusion_matrix_multiclase(
            preds, respuesta, prediction_column
        )
        knn_metrics[K] = calculate_metrics(confusion_matrix[K])

    return {
        "split": {"train": len(train), "test": len(test), "proporcion_test": 0.20},
        "KNMEDIAS-2": {
            "confusion_matrix": confusion_matrix[2],
            "accuracy": knn_metrics[2]["accuracy"],
            "recall": knn_metrics[2]["recall"],
            "precision": knn_metrics[2]["precision"],
            "f1": knn_metrics[2]["f1"],
        },
        "KNMEDIAS-3": {
            "confusion_matrix": confusion_matrix[3],
            "accuracy": knn_metrics[3]["accuracy"],
            "recall": knn_metrics[3]["recall"],
            "precision": knn_metrics[3]["precision"],
            "f1": knn_metrics[3]["f1"],
        },
        "KNMEDIAS-4": {
            "confusion_matrix": confusion_matrix[4],
            "accuracy": knn_metrics[4]["accuracy"],
            "recall": knn_metrics[4]["recall"],
            "precision": knn_metrics[4]["precision"],
            "f1": knn_metrics[4]["f1"],
        },
        "KNMEDIAS-5": {
            "confusion_matrix": confusion_matrix[5],
            "accuracy": knn_metrics[5]["accuracy"],
            "recall": knn_metrics[5]["recall"],
            "precision": knn_metrics[5]["precision"],
            "f1": knn_metrics[5]["f1"],
        },
    }
