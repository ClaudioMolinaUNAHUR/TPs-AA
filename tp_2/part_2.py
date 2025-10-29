from utils.helpers import (
    cargar_csv,
    split_test_data,
    confusion_matrix,
    f1_score,
    precision_score,
    accuracy_score,
    recall_score,
    filter_data_prestamo,
    plot_precision_vs_tree_size,
)
from tp_2.addons.functions import (
    discrete_id3,
    bootstrap_train,
    predict_random_forest_id3,
    calculate_tree_accuracy,
)


def tp2_part_2():
    file_path = "./tp_1/Préstamo.csv"
    file_path_precision = "./tp_2/results/precision_vs_tree_size.png"
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
    forest_length = 10
    random_forest = []

    result = filter_data_prestamo(data, attrs, concepto, ages=[40, 45], between=True)
    test, train = split_test_data(result, test_size=0.20)

    bootstraps = bootstrap_train(train, attrs, forest_length, q_attrs=4)

    node_counts = []
    train_accuracies = []
    test_accuracies = []

    for i in range(forest_length):

        node_count, tree = discrete_id3(
            bootstraps[i]["train"], bootstraps[i]["attrs"], concepto
        )
        node_counts.append(node_count)

        train_acc = calculate_tree_accuracy(
            tree, bootstraps[i]["train"], concepto, condicion_cumplida
        )
        test_acc = calculate_tree_accuracy(tree, test, concepto, condicion_cumplida)

        train_accuracies.append(train_acc)
        test_accuracies.append(test_acc)

        random_forest.append(tree)

    # Realizar predicciones
    predict_random_forest_id3(
        test, random_forest, condicion_cumplida, prediction_column
    )

    confusion_matrix_result, matrix, str_matrix = confusion_matrix(
        test, concepto, prediction_column, condicion_cumplida
    )

    tp = confusion_matrix_result["tp"]
    tn = confusion_matrix_result["tn"]
    fp = confusion_matrix_result["fp"]
    fn = confusion_matrix_result["fn"]

    accuracy = accuracy_score(tp, tn, fp, fn)
    recall = recall_score(tp, fn)
    precision = precision_score(tp, fp)
    f1 = f1_score(precision, recall)
    plot_precision_vs_tree_size(
        node_counts, train_accuracies, test_accuracies, file_path_precision
    )

    return {
        "accuracy": accuracy,
        "f1": f1,
        "confusion_matrix": str_matrix,
    }
