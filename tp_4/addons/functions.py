import math
import numpy as np

def euclidean_distance(point1, point2):
    result = 0
    for i in range(len(point1)):
        diff = point1[i] - point2[i]
        result += diff ** 2
    return math.sqrt(result)

def manhattan_distance(point1, point2):
    result = 0
    for i in range(len(point1)):
        diff = point1[i] - point2[i]
        result += abs(diff)
    return result

def standarize_data(data, attrs):
    media = {}
    desvio = {}
    lenght = float(len(data))
    data_standarized = []
    
    for attr in attrs:
        suma = 0
        for row in data:
            suma += row[attr]
        media[attr] = suma / lenght
        
        # Calcular varianza (reiniciar suma)
        suma_varianza = 0.0
        for row in data:
            suma_varianza += ((row[attr]) - media[attr]) ** 2
        desvio[attr] = math.sqrt(suma_varianza / (lenght - 1.0))
    
    for row in data:
        new_row = row.copy()
        for attr in attrs:
            new_row[attr] = (row[attr] - media[attr]) / desvio[attr]
        data_standarized.append(new_row)
        
    return data_standarized

def prediction_knn(train, attrs, row_test, Ks, respuesta, distance_metric="euclidean"):
    distances = []
                
    for row_train in train:
        values_train = []
        values_test = []
        for attr in attrs:
            values_train.append(row_train[attr])
            values_test.append(row_test[attr])
            
        if distance_metric == "euclidean":
            distance = euclidean_distance(values_train, values_test)
        else:
            distance = manhattan_distance(values_train, values_test)
            
        distances.append((distance, row_train[respuesta]))
    
    # ordenar de menor a mayor distancia
    distances.sort(key=lambda x: x[0])
    
    predictions = {}
    for K in Ks:
        top_k = distances[:K]
        votes = {}
        for _, label in top_k:
            if label not in votes:
                votes[label] = 0
            votes[label] += 1
        # obtener la clase con mas votos
        mayor_voto = -1
        class_prediction = None
        
        for label, count in votes.items():
            if count > mayor_voto:
                mayor_voto = count
                class_prediction = label
        predictions[K] = class_prediction
    
    return predictions

def prediction_knn_pond(train, attrs, row_test, K, respuesta):
    distances = []
                
    for row_train in train:
        values_train = []
        values_test = []
        for attr in attrs:
            values_train.append(row_train[attr])
            values_test.append(row_test[attr])
            
        distance = euclidean_distance(values_train, values_test)
        # Guardar distancia y label, luego ordenaremos por distancia
        distances.append((distance, row_train[respuesta]))
    
    # ordenar de menor a mayor distancia
    distances.sort(key=lambda x: x[0])
    
    # tomar los K vecinos más cercanos y calcular pesos
    top_k = distances[:K]
    
    # Si hay distancia 0, retornar directamente esa clase (mismo punto)
    if top_k[0][0] == 0:
        return top_k[0][1]
    
    sum_weights = {}
    for distance, label in top_k:
        # Peso inversamente proporcional al cuadrado de la distancia
        # Ya verificamos que distance > 0, así que es seguro dividir
        weight = 1 / (distance ** 2)
        
        if label not in sum_weights:
            sum_weights[label] = 0
        sum_weights[label] += weight
    
    # se obtiene la clase con mayor peso
    mayor_weight = -1
    class_prediction = None
    for label, weight in sum_weights.items():
        if weight > mayor_weight:
            mayor_weight = weight
            class_prediction = label
    
    return class_prediction
        
