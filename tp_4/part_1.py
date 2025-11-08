import sys
import os
from utils.helpers import cargar_csv, split_test_data, filter_data_wines, confusion_matrix
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

    print(best_K)
    # Verificar si best_K tiene elementos antes de usar max()
    best_K_result = {"K": None, "V": 0}
    for K, value in best_K.items():
        if best_K_result["V"] < value:
            best_K_result["V"] = value
            best_K_result["K"] = K
    
    print(best_K_result)
        
    predicted_pond = []
    for row_test in test_std:         
        result = prediction_knn_pond(train_std, attrs, row_test, best_K_result["K"], respuesta)
        predicted_pond.append({"actual": row_test[respuesta], prediction_column: result})
    print(predicted_pond)
    print(predicted)
    return
    # return {
    #     "split": {"train": len(train), "test": len(test), "proporcion_test": 0.20},
    #     "attrs": attrs,
    #     "respuesta": respuesta,
    #     "regresion_lineal": {
    #         "student_pred": y_pred_test_student_linear,
    #         "coefficient_reg": coefficient_reg,
    #         "r2_test": r2,
    #     },
    #     "respuesta_log_reg": respuesta_log_reg,
    #     "regresion_logistica": {
    #         "student_pred": y_pred_test_student_logistic[0],
    #         "coefficient_reg": LogRegression.coef_,
    #         "B0": LogRegression.intercept_,
    #         "accuracy": accuracy,
    #         "matrix": str_matrix,
    #         "confusion_matrix": {"tp": tp, "tn": tn, "fp": fp, "fn": fn},
    #         "f1": f1,
    #     },


#    }
