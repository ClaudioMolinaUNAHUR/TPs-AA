import sys
import os
from utils.helpers import (
    cargar_csv,
    split_test_data,
    filter_data_wines,
    confusion_matrix_multiclase,
    calculate_metrics,
)
from tp_4.addons.functions import standarize_data, prediction_knn, prediction_knn_pond

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def tp4_part_1():
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

    predicted = []
    Ks = [3, 5, 7]
    for row_test in test_std:
        result = prediction_knn(train_std, attrs, row_test, Ks, respuesta)
        predicted.append({"actual": row_test[respuesta], prediction_column: result})

    best_K = {}

    for index in range(len(predicted)):
        actual = predicted[index]["actual"]
        prediction = predicted[index][prediction_column]
        for K, label in prediction.items():
            if K not in best_K:
                best_K[K] = 0
            if label == actual:
                best_K[K] += 1


    # Verificar si best_K tiene elementos antes de usar max()
    best_K_result = {"K": None, "V": 0}
    for K, value in best_K.items():
        if best_K_result["V"] < value:
            best_K_result["V"] = value
            best_K_result["K"] = K

    predicted_pond = []
    for row_test in test_std:
        result = prediction_knn_pond(
            train_std, attrs, row_test, best_K_result["K"], respuesta
        )
        predicted_pond.append(
            {"actual": row_test[respuesta], prediction_column: result}
        )
    # Crear una copia profunda de las predicciones para el mejor K
    predicted_best_K = []
    for pred in predicted:
        predicted_best_K.append({
            "actual": pred["actual"],
            prediction_column: pred[prediction_column][best_K_result["K"]]
        })

    confusion_matrix_knn = confusion_matrix_multiclase(
        predicted_best_K, "actual", prediction_column
    )
    confusion_matrix_knn_pond = confusion_matrix_multiclase(
        predicted_pond, "actual", prediction_column
    )
    knn_metrics = calculate_metrics(confusion_matrix_knn)
    knn_pond_metrics = calculate_metrics(confusion_matrix_knn_pond)

    return {
        "split": {"train": len(train), "test": len(test), "proporcion_test": 0.20},
        "KNN": {
            "confusion_matrix": confusion_matrix_knn,
            "accuracy": knn_metrics["accuracy"],
            "recall": knn_metrics["recall"],
            "precision": knn_metrics["precision"],
            "f1": knn_metrics["f1"],
        },
        "KNN-POND": {
            "confusion_matrix": confusion_matrix_knn_pond,
            "accuracy": knn_pond_metrics["accuracy"],
            "recall": knn_pond_metrics["recall"],
            "precision": knn_pond_metrics["precision"],
            "f1": knn_pond_metrics["f1"],
        },
    }
