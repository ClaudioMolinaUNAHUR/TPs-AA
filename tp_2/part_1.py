from utils.helpers import cargar_csv, split_test_data
from tp_1.addons.functions import filter_data_prestamo
from collections import Counter, defaultdict
import math


def tp2_part_1():
    file_path = "./tp_1/Préstamo.csv"
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

    result = filter_data_prestamo(data, attrs, concepto, ages=[40, 45], between=True)
    test, train = split_test_data(result, test_size=0.20)
    tree = id3(train, attrs, concepto)
    #print(tree)
    result = []
    for row in test:
        clase = evaluate_id3(row, tree)
        row[prediction_column] = 1 if condicion_cumplida == clase else 0
        result.append(row)
    print(result)
    # print(len(test), len(train), len(result), hipotesis)

    return result


# =========================
# Entropía 
# =========================
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

def evaluate_id3(data, tree):
    esdict = isinstance(tree, dict)
    
    if not esdict:
        print(f"Clase terminal encontrada: {tree}")
        return tree
    
    for key, value in tree.items():
        if data[key] in value.keys():
            return evaluate_id3(data, value[data[key]])
    
    return None


# =========================
# Ganancia de información
# =========================
def ganancia_informacion(data, attr, target_attr):
    total = len(data)
    # entropía original
    base_entropy = entropia(data, target_attr) # H(D) donde D es el conjunto de datos del nodo
    # valores del atributo
    valores = set(row[attr] for row in data)
    # valores = {"lluvioso", "soleado", "ventoso"}
    # entropía condicional
    children_entropy = 0 # H(D|Ax) donde x es target_attr
    for val in valores:
        subset = [row for row in data if row[attr] == val]
        children_entropy += (len(subset) / total) * entropia(subset, target_attr)
    return base_entropy - children_entropy

# =========================
# ID3
# =========================
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
    arbol = {mejor_attr: {}}

    #se crea conjunto de valores que toma ese atributo mejor rankeado dentro del conjunto de datos
    set_values = set()
    for row in data:
        set_values.add(row[mejor_attr])
    
    for value in set_values:
        # se crea nuevo lista de datos, con los datos filtrados por cada uno de los valores
        # que toma ese atributo
        filter_attr = []
        for row in data:
            if row[mejor_attr] == value:
                filter_attr.append(row)
                
        if not filter_attr:
            # si no hay datos, usar clase mayoritaria
            arbol[mejor_attr][value] = mayoritary_class(clases)
        else:
            # se crea nueva lista de atributos sin el mejor, porque ya se consulto
            nuevos_attrs = []
            for attr in attrs:
                if attr != mejor_attr:
                    nuevos_attrs.append(attr)
            
            arbol[mejor_attr][value] = id3(filter_attr, nuevos_attrs, target_attr)

    return arbol

def mayoritary_class(clases):
    # devuelve el valor maximo de clase en ese nodo
    counter = Counter(clases)
    max_value = float('-inf')
    class_value = ""
    for clase, value in counter.items():
        if value > max_value:
            max_value = value
            class_value = clase 
            
    return class_value

        
    
    
{
    "Préstamos previos impagos": {
        "NO": {
            "Estado de vivienda": {
                "INQUILINO": {
                    "Mayor nivel educativo": {
                        "TERCIARIO": {
                            "Destino de los fondos": {
                                "EMPRESA": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "PERSONAL": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "SALUD": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "EDUCACION": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "DEUDAS": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "OTORGADO",
                                    }
                                },
                                "VIVIENDA": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "OTORGADO",
                                    }
                                },
                            }
                        },
                        "SECUNDARIO": {
                            "Destino de los fondos": {
                                "EMPRESA": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "OTORGADO",
                                    }
                                },
                                "PERSONAL": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "OTORGADO",
                                    }
                                },
                                "SALUD": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "OTORGADO",
                                    }
                                },
                                "EDUCACION": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "OTORGADO",
                                    }
                                },
                                "DEUDAS": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "OTORGADO",
                                    }
                                },
                                "VIVIENDA": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "OTORGADO",
                                    }
                                },
                            }
                        },
                        "UNIVERSITARIO": {
                            "Destino de los fondos": {
                                "EMPRESA": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "PERSONAL": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "SALUD": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "EDUCACION": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "DEUDAS": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "VIVIENDA": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "OTORGADO",
                                    }
                                },
                            }
                        },
                        "MAESTRíA": {
                            "Destino de los fondos": {
                                "EMPRESA": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "PERSONAL": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "SALUD": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "OTORGADO",
                                    }
                                },
                                "EDUCACION": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "OTORGADO",
                                    }
                                },
                                "DEUDAS": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "VIVIENDA": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "OTORGADO",
                                    }
                                },
                            }
                        },
                        "DOCTORADO": {
                            "Destino de los fondos": {
                                "EMPRESA": "RECHAZADO",
                                "PERSONAL": "RECHAZADO",
                                "SALUD": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "EDUCACION": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "OTORGADO",
                                    }
                                },
                                "VIVIENDA": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "OTORGADO",
                                    }
                                },
                            }
                        },
                    }
                },
                "HIPOTECA": {
                    "Destino de los fondos": {
                        "EMPRESA": {
                            "Mayor nivel educativo": {
                                "TERCIARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "SECUNDARIO": {"Sexo": {"MASCULINO": "RECHAZADO"}},
                                "UNIVERSITARIO": "RECHAZADO",
                                "MAESTRíA": "RECHAZADO",
                                "DOCTORADO": "RECHAZADO",
                            }
                        },
                        "PERSONAL": {
                            "Mayor nivel educativo": {
                                "TERCIARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "SECUNDARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "UNIVERSITARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "OTORGADO",
                                    }
                                },
                                "MAESTRíA": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "DOCTORADO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "OTORGADO",
                                    }
                                },
                            }
                        },
                        "SALUD": {
                            "Mayor nivel educativo": {
                                "TERCIARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "SECUNDARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "UNIVERSITARIO": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "MAESTRíA": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "DOCTORADO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                            }
                        },
                        "EDUCACION": {
                            "Mayor nivel educativo": {
                                "SECUNDARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "UNIVERSITARIO": "RECHAZADO",
                                "MAESTRíA": "OTORGADO",
                                "DOCTORADO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "TERCIARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                            }
                        },
                        "DEUDAS": {
                            "Mayor nivel educativo": {
                                "TERCIARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "SECUNDARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "OTORGADO",
                                    }
                                },
                                "UNIVERSITARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "MAESTRíA": "RECHAZADO",
                                "DOCTORADO": "OTORGADO",
                            }
                        },
                        "VIVIENDA": {
                            "Mayor nivel educativo": {
                                "UNIVERSITARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "OTORGADO",
                                    }
                                },
                                "SECUNDARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                                "DOCTORADO": "RECHAZADO",
                                "TERCIARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                            }
                        },
                    }
                },
                "OTRO": {
                    "Mayor nivel educativo": {
                        "UNIVERSITARIO": "RECHAZADO",
                        "SECUNDARIO": "OTORGADO",
                        "TERCIARIO": {
                            "Destino de los fondos": {
                                "PERSONAL": "OTORGADO",
                                "EDUCACION": "OTORGADO",
                                "VIVIENDA": "RECHAZADO",
                            }
                        },
                    }
                },
                "PROPIETARIO": {
                    "Mayor nivel educativo": {
                        "TERCIARIO": {
                            "Destino de los fondos": {
                                "PERSONAL": "RECHAZADO",
                                "EDUCACION": {"Sexo": {"MASCULINO": "OTORGADO"}},
                                "EMPRESA": "RECHAZADO",
                                "SALUD": "RECHAZADO",
                            }
                        },
                        "SECUNDARIO": {
                            "Destino de los fondos": {
                                "EMPRESA": "RECHAZADO",
                                "PERSONAL": "RECHAZADO",
                                "SALUD": {"Sexo": {"MASCULINO": "RECHAZADO"}},
                                "EDUCACION": "RECHAZADO",
                                "VIVIENDA": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "RECHAZADO",
                                    }
                                },
                            }
                        },
                        "UNIVERSITARIO": "RECHAZADO",
                        "MAESTRíA": "RECHAZADO",
                        "DOCTORADO": "OTORGADO",
                    }
                },
            }
        },
        "SI": "RECHAZADO",
    }
}
