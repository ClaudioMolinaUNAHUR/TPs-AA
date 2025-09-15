from collections import Counter
import math


def evaluate_id3(data, tree):
    esdict = isinstance(tree, dict)

    if not esdict:
        return tree

    for key, value in tree.items():   
        if key != "metrics" and data[key] in value.keys():
            return evaluate_id3(data, value[data[key]])

    return None


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


def id3(data, attrs, target_attr):
    clases = [row[target_attr] for row in data]

    # Caso 1: todas las instancias son de la misma clase
    if len(set(clases)) == 1:
        return clases[0]

    # Caso 2: no hay más atributos
    if not attrs:
        return mayoritary_class(clases)

    # Caso 3: escoger el mejor atributo según ganancia de información
    mejor_attr = max(attrs, key=lambda a: ganancia_informacion(data, a, target_attr))

    # crear el nodo del árbol
    arbol = {mejor_attr: {}, "metrics": {"IG": ganancia_informacion(data, mejor_attr, target_attr), "Class": Counter(clases)}}

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
            # si no hay datos, usar clase mayoritaria
            arbol[mejor_attr][value] = mayoritary_class(clases)
        else:
            # se crea nueva lista de atributos sin el mejor, porque ya se consulto
            nuevos_attrs = []
            for attr in attrs:
                if attr != mejor_attr:
                    nuevos_attrs.append(attr)

            arbol[mejor_attr][value] = id3(filter_by_value, nuevos_attrs, target_attr)

    return arbol


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
