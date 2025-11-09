import sys
import os
from utils.helpers import (
    cargar_csv,
    split_test_data,
    filter_data_wines,
    confusion_matrix_multiclase,
    calculate_metrics
)
from tp_4.addons.functions import knn_mean, standarize_data, prediction_knn,  knn_mean, predict_kmeans

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

    Ks =[3,5,7]


    prediction = {}
    predicted = []
    for K in Ks:
        clusters = knn_mean(train_std,attrs, K)
        for row in test_std:
        
             
            row[prediction_column] = predict_kmeans(train_std, row, attrs, respuesta, clusters)

   
    for row in test_std:
        row[prediction_column] = prediction[K]
        predicted.append(row)
    confusion_matrix = confusion_matrix_multiclase(
        test_std, respuesta, prediction_column
    )

    print("Matriz de confusión para KNN:", confusion_matrix)
    knn_metrics = calculate_metrics(confusion_matrix)
    print("Métricas para KNN:", knn_metrics)

    return