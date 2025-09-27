from utils.helpers import (
    cargar_csv,
    split_test_data,
    confusion_matrix,
    f1_score,
    precision_score,
    accuracy_score,
    recall_score,
    filter_data_prestamo,
    save_json,
)
from tp_2.addons.functions import discrete_id3, bootstrap_train, predict_random_forest_id3
import random


def tp2_part_2():
    file_path = "./tp_1/Préstamo.csv"
    file_path_tree = "./tp_2/tree.json"
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
    forrest_length = 10
    random_forrest = []
    
    result = filter_data_prestamo(data, attrs, concepto, ages=[40, 45], between=True)
    test, train = split_test_data(result, test_size=0.20)
        
    bootstraps = bootstrap_train(train, attrs, forrest_length)
    for i in range(forrest_length):        
        print(len(bootstraps[i]["attrs"]))
        print(len(bootstraps[i]["train"]))

    print("test: ", len(test))
    print("train: ", len(train))
    print("total: ", len(result))

    for i in range(forrest_length):
        quantity, tree = discrete_id3(bootstraps[i]["train"], bootstraps[i]["attrs"], concepto)
        random_forrest.append(tree)
    

    predicted = []
    predict_random_forest_id3(test, random_forrest, condicion_cumplida, prediction_column)
    print(test)

    # confusion_matrix_result = confusion_matrix(
    #     predicted, concepto, prediction_column, condicion_cumplida
    # )

    # tp = confusion_matrix_result["tp"]
    # tn = confusion_matrix_result["tn"]
    # fp = confusion_matrix_result["fp"]
    # fn = confusion_matrix_result["fn"]

    # accuracy = accuracy_score(tp, tn, fp, fn)
    # recall = recall_score(tp, fn)
    # precision = precision_score(tp, fp)
    # f1 = f1_score(precision, recall)
    # return {
    #     "accuracy": accuracy,
    #     "f1": f1,
    #     "confusion_matrix": confusion_matrix_result,
    # }
