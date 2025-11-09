import math
import numpy as np
import random

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

def knn_mean(train, attrs, K, max_iteraciones=100):
    """
    Entrena K-means clustering siguiendo los pasos del algoritmo:
    
    Paso 1: Elegir la cantidad de clusters (K se pasa como parámetro).
    Paso 2: Elegir aleatoriamente K puntos diferentes que definen los clusters iniciales.
    Paso 3: Calcular las distancias de cada uno de los puntos a los K puntos seleccionados.
    Paso 4: Asignar a cada uno de los puntos el cluster más cercano considerando las distancias.
    Paso 5: Calcular los centroides de cada uno de los clusters obtenidos.
    
    Los pasos 3, 4 y 5 se repiten hasta convergencia o max_iteraciones.
    
    Retorna: diccionario con los clusters entrenados
    """
    # Paso 1: Elegir la cantidad de clusters (K viene como parámetro)
    # K = 3, 5, 7, etc.
    
    # Paso 2: Elegir aleatoriamente K puntos diferentes que definen los clusters iniciales
  
    indices_aleatorios = random.sample(range(len(train)), K)
    
    # Crear los centros iniciales extrayendo los valores de los atributos
    clusters = {}
    for i, idx in enumerate(indices_aleatorios):
        centro = []
        for attr in attrs:
            centro.append(train[idx][attr])
        clusters[i] = {
            'centro': centro,  # Centroide inicial del cluster
            'puntos': []  # Lista de índices de puntos asignados a este cluster
        }
    
    # Iterar hasta convergencia (repetir pasos 3, 4 y 5)
    for iteracion in range(max_iteraciones):
        # Limpiar asignaciones anteriores
        for cluster_id in clusters:
            clusters[cluster_id]['puntos'] = []
        
        # Paso 3: Calcular las distancias de cada uno de los puntos a los K puntos 
        # seleccionados en el paso anterior (centros de clusters)
        # Matriz de distancias: para cada punto, guardar distancia a cada cluster
        matriz_distancias = []  # Lista de listas: [punto_idx][(distancia, cluster_id)]
        
        # Para cada punto en el dataset de entrenamiento
        for idx, row in enumerate(train):
            # Extraer los valores del punto (solo los atributos)
            punto = []
           
            for attr in attrs:
                punto.append(row[attr])
            
            # Calcular distancia de este punto a cada uno de los K centros
            distancias_punto = []
            for cluster_id, cluster_data in clusters.items():
                punto_a = punto.copy() # registro de train, solo valores de atributos
                punto_b = cluster_data['centro'].copy() #Registro de cada centroide
                # Calcular distancia euclidiana entre el punto y el centro del cluster
                distancia = euclidean_distance(punto_a, punto_b)
                distancias_punto.append((distancia, cluster_id))
            
            # Guardar todas las distancias de este punto a los K centros
            matriz_distancias.append(distancias_punto)
        
        # Paso 4: Asignar a cada uno de los puntos el cluster más cercano 
        # considerando las distancias calculadas en el paso anterior
        for idx, distancias_punto in enumerate(matriz_distancias):
            # Ordenar distancias de menor a mayor
            distancias_punto.sort(key=lambda x: x[0])
            # Asignar al cluster más cercano (el de menor distancia)
            cluster_mas_cercano = distancias_punto[0][1]
            # se va a guardar que registro esta más proximo a cada centroide en lista de puntos de cada cluster
            clusters[cluster_mas_cercano]['puntos'].append(idx)
        
        # Paso 5: Calcular los centroides de cada uno de los clusters obtenidos 
        # en el paso anterior
        # El centroide es el promedio (media) de todos los puntos en el cluster
        centros_anteriores = {}
        convergio = True
        
        for cluster_id, cluster_data in clusters.items():
            # Guardar centro anterior para verificar convergencia
            centros_anteriores[cluster_id] = cluster_data['centro'].copy()
            
            # Calcular nuevo centroide como promedio de los puntos asignados al cluster
            puntos_cluster = cluster_data['puntos']
            if len(puntos_cluster) > 0:
                nuevo_centroide = []
                # Para cada atributo, calcular la media de todos los puntos del cluster
                for i, attr in enumerate(attrs):
                    suma = 0
                    for idx in puntos_cluster:
                        suma += train[idx][attr]
                    nuevo_centroide.append(suma / len(puntos_cluster))
                clusters[cluster_id]['centro'] = nuevo_centroide
                
                # Verificar si el centroide cambió significativamente (convergencia)
                for i in range(len(attrs)):
                    abs_diff = abs(clusters[cluster_id]['centro'][i] - centros_anteriores[cluster_id][i])
                    if abs_diff > 0.0001:
                        convergio = False
            else:
                # Si un cluster está vacío, mantener el centro anterior
                convergio = False
        
        # Si convergió (los centroides no cambian), salir del bucle
        if convergio:
            break
    
    return clusters

def predict_kmeans(train, row_test, attrs, respuesta, clusters):
    """
    Predice la clase de un punto de prueba usando clusters entrenados.
    
    Asigna el punto al cluster más cercano y retorna la clase más común
    en ese cluster.
    """
    # Extraer los valores del punto de prueba
    punto_test = []
    for attr in attrs:
        punto_test.append(row_test[attr])
    
    # Encontrar el cluster más cercano
    distancias_a_centros = []
    for cluster_id, cluster_data in clusters.items():
        punto_test_a = punto_test.copy()
        punto_cluster_b = cluster_data['centro'].copy()
        distancia = euclidean_distance(punto_test_a, punto_cluster_b)
        distancias_a_centros.append((distancia, cluster_id))
    
    # Ordenar por distancia y obtener el cluster más cercano
    distancias_a_centros.sort(key=lambda x: x[0])
    cluster_mas_cercano_id = distancias_a_centros[0][1]
    
    # Encontrar la clase más común en ese cluster
    puntos_cluster = clusters[cluster_mas_cercano_id]['puntos']
    
 
 # Contar las clases en los puntos del cluster
    clases = {}
    for idx in puntos_cluster:
        clase = train[idx][respuesta]
        if clase not in clases:
            clases[clase] = 0
        clases[clase] += 1
        
    # Retornar la clase más común (usar max aquí es correcto)
    clase_predicha = max(clases.items(), key=lambda x: x[1])[0]
   
    
    return clase_predicha

