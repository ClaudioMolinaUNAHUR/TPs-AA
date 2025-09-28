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
    forrest_length = 10
    random_forrest = []

    result = filter_data_prestamo(data, attrs, concepto, ages=[40, 45], between=True)
    test, train = split_test_data(result, test_size=0.20)

    bootstraps = bootstrap_train(train, attrs, forrest_length, q_attrs=4)

    print("=== CONFIGURACIÓN RANDOM FOREST ===")
    print(f"Número de árboles: {forrest_length}")
    print(f"Atributos originales: {len(attrs)}")
    print(f"Test: {len(test)} muestras")
    print(f"Train: {len(train)} muestras")
    print(f"Total: {len(result)} muestras")
    print()

    node_counts = []
    train_accuracies = []
    test_accuracies = []

    for i in range(forrest_length):
        print(f"  - Atributos seleccionados: {len(bootstraps[i]['attrs'])}")
        print(f"  - Muestras bootstrap: {len(bootstraps[i]['train'])}")

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

        random_forrest.append(tree)
        print(f"  - Nodos internos: {node_count}")
        print(f"  - Precisión entrenamiento: {train_acc:.4f}")
        print(f"  - Precisión prueba: {test_acc:.4f}")
        print(f"  - Atributos usados: {bootstraps[i]['attrs']}")
        print()

    print(f"=== ANÁLISIS DEL BOSQUE ===")
    print(f"Conteos individuales: {node_counts}")
    print()

    # Realizar predicciones
    predict_random_forest_id3(
        test, random_forrest, condicion_cumplida, prediction_column
    )

    confusion_matrix_result = confusion_matrix(
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

    print("=== RESULTADOS ===")
    print(f"Matriz de confusión: TP={tp}, TN={tn}, FP={fp}, FN={fn}")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-Score: {f1:.4f}")

    return {
        "accuracy": accuracy,
        "f1": f1,
        "confusion_matrix": confusion_matrix_result,
    }
