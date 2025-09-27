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
from tp_2.addons.functions import discrete_id3, bootstrap_train, predict_random_forest_id3, predict_id3
import math
import matplotlib.pyplot as plt
import numpy as np


def calculate_tree_accuracy(tree, data, concepto, condicion_cumplida):

    correct_predictions = 0
    total_predictions = len(data)
    
    for row in data:
        prediction = predict_id3(row, tree)
        actual = row[concepto]
        
     
        predicted_binary = 1 if prediction == condicion_cumplida else 0
        actual_binary = 1 if actual == condicion_cumplida else 0
        
        if predicted_binary == actual_binary:
            correct_predictions += 1
    
    return correct_predictions / total_predictions if total_predictions > 0 else 0

def plot_precision_vs_tree_size(node_counts, train_accuracies, test_accuracies):
   
    plt.figure(figsize=(10, 6))
    
    
    sorted_indices = np.argsort(node_counts)
    sorted_nodes = [node_counts[i] for i in sorted_indices]
    sorted_train_acc = [train_accuracies[i] for i in sorted_indices]
    sorted_test_acc = [test_accuracies[i] for i in sorted_indices]
    

    plt.plot(sorted_nodes, sorted_train_acc, 'o-', label='Entrenamiento', color='blue', linewidth=2, markersize=6)
    plt.plot(sorted_nodes, sorted_test_acc, 's-', label='Prueba', color='red', linewidth=2, markersize=6)
    

    plt.xlabel('Número de Nodos Internos del Árbol', fontsize=12)
    plt.ylabel('Precisión', fontsize=12)
    plt.title('Precisión vs Tamaño del Árbol\n(Entrenamiento vs Prueba)', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    
   
    all_accuracies = sorted_train_acc + sorted_test_acc
    plt.ylim(min(all_accuracies) - 0.05, min(1.0, max(all_accuracies) + 0.05))
    
   
    if len(sorted_nodes) > 0:
        min_nodes = min(node_counts)
        max_nodes = max(node_counts)
        
        plt.annotate(f'Min: {min_nodes} nodos', 
                    xy=(min_nodes, min(train_accuracies)), 
                    xytext=(10, 10), textcoords='offset points',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7),
                    fontsize=9)
        
        plt.annotate(f'Max: {max_nodes} nodos', 
                    xy=(max_nodes, max(train_accuracies)), 
                    xytext=(10, -20), textcoords='offset points',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.7),
                    fontsize=9)
    
    plt.tight_layout()
    plt.savefig('./tp_2/precision_vs_tree_size.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("Gráfico guardado como: ./tp_2/precision_vs_tree_size.png")


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
    train_accuracies = [] 
    test_accuracies = [] 
    
    for i in range(forrest_length):
        print(f"Entrenando árbol {i+1}/{forrest_length}...")
        print(f"  - Atributos seleccionados: {len(bootstraps[i]['attrs'])}")
        print(f"  - Muestras bootstrap: {len(bootstraps[i]['train'])}")
        
        node_count, tree = discrete_id3(bootstraps[i]["train"], bootstraps[i]["attrs"], concepto)
        node_counts.append(node_count)  
        
      
        train_acc = calculate_tree_accuracy(tree, bootstraps[i]["train"], concepto, condicion_cumplida)
        test_acc = calculate_tree_accuracy(tree, test, concepto, condicion_cumplida)
        
        train_accuracies.append(train_acc)
        test_accuracies.append(test_acc)
        
        random_forrest.append(tree)
        print(f"  - Nodos internos: {node_count}")
        print(f"  - Precisión entrenamiento: {train_acc:.4f}")
        print(f"  - Precisión prueba: {test_acc:.4f}")
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
    
    
    plot_precision_vs_tree_size(node_counts, train_accuracies, test_accuracies)
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
