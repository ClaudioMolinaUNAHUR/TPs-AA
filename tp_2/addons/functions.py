from collections import Counter
import math
import random


def predict_id3(data, tree):
    if not isinstance(tree, dict):
        return tree  # Es una hoja, devuelve la clase.

    # Encontrar el atributo de este nodo (la clave que no es 'metrics')
    attribute = None
    for key in tree:
        if key != 'metrics':
            attribute = key
            break  # Encontramos el atributo, salimos del bucle

    if attribute is None:
        # No se encontró un atributo para dividir, usar la clase mayoritaria
        class_counts = tree['metrics']['class']
        return max(class_counts, key=class_counts.get)

    value_in_data = data.get(attribute)

    # Si el valor del dato existe como una rama en el árbol, la seguimos.
    if value_in_data in tree[attribute]:
        return predict_id3(data, tree[attribute][value_in_data])
    else:
        # Dato no visto: no hay rama. Devolvemos la clase mayoritaria de este nodo.
        class_counts = tree['metrics']['class']
        return max(class_counts, key=class_counts.get)


def predict_random_forest_id3(data, forrest, condicion_cumplida, prediction_column):

    for row in data:
        predictions = []
        for tree in forrest:
            clase = predict_id3(row, tree)
            if clase is not None:
                predictions.append(1 if condicion_cumplida == clase else 0)
            else:

                predictions.append(0)

        positive_votes = sum(predictions)
        total_votes = len(predictions)
        prediction = positive_votes / total_votes if total_votes > 0 else 0

        row[prediction_column] = 1 if prediction >= 0.5 else 0


def entropia(data, target_attr):
    total = len(data)
    if total == 0:
        return 0
    sum = 0.0
    data_row = []
    for row in data:
        data_row.append(row[target_attr])
    conteo = Counter(data_row)
    for value_count in conteo.values():
        sum += -(value_count / total) * math.log2(value_count / total)
    return sum


def ganancia_informacion(data, attr, target_attr):
    total = len(data)
    # entropía original
    base_entropy = entropia(
        data, target_attr
    )  # H(D) donde D es el conjunto de datos del nodo
    # valores del atributo
    valores = set(row[attr] for row in data)
    # valores = {"FEMENINO", "MASCULINO"} Sexo, pueden aparecer ambos o ninguno, depende de data
    # entropía condicional
    children_entropy = 0  # H(D|Ax) donde x es attr (Ejemplo: Sexo)
    for val in valores:
        subset = [row for row in data if row[attr] == val]
        children_entropy += (len(subset) / total) * entropia(subset, target_attr)
    return base_entropy - children_entropy


def discrete_id3(data, attrs, target_attr):
    clases = [row[target_attr] for row in data]

    if len(set(clases)) == 1:
        return 0, {"class": clases[0], "metrics": {"entropy": 0, "count": len(clases)}}

    if not attrs:
        return 0, mayoritary_class(clases)

    # escoger el mejor atributo según ganancia de información
    mejor_attr = max(attrs, key=lambda a: ganancia_informacion(data, a, target_attr))

    # crear el nodo del árbol
    arbol = {
        mejor_attr: {},
        "metrics": {
            "entropy": entropia(data, target_attr),
            "class": Counter(clases),
        },
    }

    node_count = 1

    # se crea conjunto de valores que toma ese atributo mejor rankeado dentro del conjunto de datos
    set_values = set()
    for row in data:
        set_values.add(row[mejor_attr])

    for value in set_values:
        # se crea nuevo lista de datos, con los datos filtrados por cada uno de los valores
        # que toma ese atributo
        filter_by_value = []
        for row in data:
            if row[mejor_attr] == value:
                filter_by_value.append(row)

        if not filter_by_value:

            arbol[mejor_attr][value] = mayoritary_class(clases)
        else:
            # se crea nueva lista de atributos sin el mejor, porque ya se consulto
            nuevos_attrs = []
            for attr in attrs:
                if attr != mejor_attr:
                    nuevos_attrs.append(attr)
            sub_count, result = discrete_id3(filter_by_value, nuevos_attrs, target_attr)
            node_count += sub_count
            if isinstance(result, dict) and "class" in result:
                arbol[mejor_attr][value] = result["class"]
                arbol["metrics"].setdefault("pure_children", []).append(
                    {"value": value, "entropy": 0, "count": result["metrics"]["count"]}
                )
            else:
                arbol[mejor_attr][value] = result

    return node_count, arbol


def mayoritary_class(clases):
    # devuelve el valor maximo de clase en ese nodo
    counter = Counter(clases)
    max_value = float("-inf")
    class_value = ""
    for clase, value in counter.items():
        if value > max_value:
            max_value = value
            class_value = clase

    return class_value


def bootstrap_train(train, attrs, forrest_length, q_attrs=0, func_sqrt=True):

    bootstraps = []
    len_train = len(train)
    use_sqrt = False
    if q_attrs == 0:
        use_sqrt = True
        # raiz de a | log de a
        q_attrs = math.log(len(attrs), 2) if func_sqrt else math.sqrt(len(attrs))
        q_attrs = max(1, int(q_attrs))  

    for i in range(forrest_length):
        selected_attrs = []
        
        #Mezclar Atributos
        shuffled_attrs = attrs.copy()
        random.shuffle(shuffled_attrs)
        
        for attr in shuffled_attrs:
            random_value = random.random()
            if len(selected_attrs) < q_attrs or (not use_sqrt and random_value >= 0.5):
                selected_attrs.append(attr)

        bootstrap_sample = []
        for _ in range(len_train):
            select_pos = random.randint(0, len_train - 1)
            bootstrap_sample.append(train[select_pos])

        bootstraps.append({"attrs": selected_attrs, "train": bootstrap_sample})

    return bootstraps


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
