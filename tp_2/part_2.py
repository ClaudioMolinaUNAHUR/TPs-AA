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
import math




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
        
 
    
    
    q_attrs = max(1, int(math.sqrt(len(attrs))))
    
   
    
    bootstraps = bootstrap_train(train, attrs, forrest_length, q_attrs)
    
    print("=== CONFIGURACIÓN RANDOM FOREST ===")
    print(f"Número de árboles: {forrest_length}")
    print(f"Atributos originales: {len(attrs)}")
    print(f"Atributos por árbol: {q_attrs} (√{len(attrs)} = {math.sqrt(len(attrs)):.2f})")
    print(f"Test: {len(test)} muestras")
    print(f"Train: {len(train)} muestras")
    print(f"Total: {len(result)} muestras")
    print()

   
    node_counts = [] 
    for i in range(forrest_length):
        print(f"Entrenando árbol {i+1}/{forrest_length}...")
        print(f"  - Atributos seleccionados: {len(bootstraps[i]['attrs'])}")
        print(f"  - Muestras bootstrap: {len(bootstraps[i]['train'])}")
        
        node_count, tree = discrete_id3(bootstraps[i]["train"], bootstraps[i]["attrs"], concepto)
        node_counts.append(node_count)  
        
        random_forrest.append(tree)
        print(f"  - Nodos internos: {node_count}")
        print(f"  - Atributos usados: {bootstraps[i]['attrs']}")
        print()
    
   
    total_nodes = sum(node_counts)
    min_nodes = min(node_counts)
    max_nodes = max(node_counts)
    avg_nodes = total_nodes / forrest_length
    
    print(f"=== ANÁLISIS DEL BOSQUE ===")
    print(f"Conteos individuales: {node_counts}")
    print(f"Total de nodos internos: {total_nodes}")
    print(f"Mínimo nodos por árbol: {min_nodes}")
    print(f"Máximo nodos por árbol: {max_nodes}")
    print(f"Promedio de nodos por árbol: {avg_nodes:.1f}")
    print(f"Desviación estándar: {(sum((x - avg_nodes)**2 for x in node_counts) / len(node_counts))**0.5:.1f}")
    print()

    # Realizar predicciones
    print("Realizando predicciones...")
    predict_random_forest_id3(test, random_forrest, condicion_cumplida, prediction_column)

    # Calcular métricas de evaluación
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
    
    print("=== RESULTADOS ===")
    print(f"Matriz de confusión: TP={tp}, TN={tn}, FP={fp}, FN={fn}")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-Score: {f1:.4f}")
    
    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "confusion_matrix": confusion_matrix_result,
    }
