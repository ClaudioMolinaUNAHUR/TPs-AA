# ind
# 50 años "Edad"
# sexo "Sexo"
# educacion "Mayor nivel educativo"
# vivienda "Estado de vivienda"
# posee prestamo "Préstamos previos impagos"

# dep
# estado "Estado"
import numpy as np
from utils.helpers import accuracy_score, split_test_data, cargar_csv


def run_find_s():
    file_path = "./tp_1/Préstamo.csv"
    data = cargar_csv(file_path, "latin-1")

    
    attr = ["Sexo", "Mayor nivel educativo", "Estado de vivienda", "Préstamos previos impagos"]
    concepto = "Estado"
    verdad = "OTORGADO"
    
    result = filter_data_prestamo(data, attr, concepto, age=50)
    hipotesis = get_hipotesis_find_s(result, attr, concepto, verdad)
    
    test, train = split_test_data(result, test_size=0.2)
    print(len(test), len(train), len(result), hipotesis)

    return hipotesis   

def get_hipotesis_find_s(result, attr, concepto, verdad):
    hipotesis = ["0"] * len(attr)
    
    for item in result:
        if item[concepto] == verdad: 
            for i, h in enumerate(hipotesis):
                if h == "0":
                    hipotesis[i] = item[attr[i]]
                elif h == item[attr[i]]:
                    continue
                else:
                    hipotesis[i] = "?"
    return hipotesis 
 

def filter_data_prestamo(data, attr, concepto, age):
    result = []
    for row in data:
        if int(row["Edad"]) == age:
            result.append(
                {
                    attr[0]: row["Sexo"],
                    attr[1]: row["Mayor nivel educativo"],
                    attr[2]: row["Estado de vivienda"],
                    attr[3]: row["Préstamos previos impagos"],
                    concepto: row["Estado"],
                }
            )
    return result

