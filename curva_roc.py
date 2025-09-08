#!/usr/bin/env python3
"""
Script para generar la curva ROC con los datos reales del modelo de Naive Bayes
"""

from tp_1.part_3 import part_3

def main():
    print("=== Generando Curva ROC  ===")
    print("Ejecutando algoritmo de Naive Bayes...")
    
    # Ejecutar el algoritmo de Naive Bayes
    resultado = part_3()
    
    # Mostrar métricas del modelo
    print(f"\n📊 Métricas del Modelo:")
    print(f"   • AUC (Área bajo la curva ROC): {resultado['roc']['auc']:.3f}")
    print(f"   • Accuracy: {resultado['accuracy']:.3f}")
    print(f"   • F1-Score: {resultado['f1']:.3f}")
    
    # Mostrar matriz de confusión
    cm = resultado['confusion_matrix']
    print(f"\n🔍 Matriz de Confusión:")
    print(f"   • Verdaderos Positivos (TP): {cm['tp']}")
    print(f"   • Verdaderos Negativos (TN): {cm['tn']}")
    print(f"   • Falsos Positivos (FP): {cm['fp']}")
    print(f"   • Falsos Negativos (FN): {cm['fn']}")
    
    # Interpretación del AUC
    auc = resultado['roc']['auc']
    if auc > 0.8:
        interpretacion = "Excelente"
    elif auc > 0.7:
        interpretacion = "Bueno"
    elif auc > 0.6:
        interpretacion = "Regular"
    elif auc > 0.5:
        interpretacion = "Pobre"
    else:
        interpretacion = "Muy pobre (peor que aleatorio)"
    
    print(f"\n📈 Interpretación del AUC: {interpretacion}")
    print(f"   El modelo tiene un rendimiento {interpretacion.lower()}.")
    
    print(f"\n✅ La curva ROC se ha generado y guardado como 'roc_curve_naive_bayes.png'")
    print(f"   Puedes abrir el archivo para ver la visualización.")

if __name__ == "__main__":
    main()
