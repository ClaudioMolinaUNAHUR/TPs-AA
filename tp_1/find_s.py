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

    attrs = [
        "Sexo",
        "Mayor nivel educativo",
        "Estado de vivienda",
        "Préstamos previos impagos",
    ]
    concepto = "Estado"
    condicion_cumplida = "OTORGADO"

    result = filter_data_prestamo(data, attrs, concepto, age=50)
    hipotesis = get_hipotesis_find_s(result, attrs, concepto, condicion_cumplida)

    test, train = split_test_data(result, test_size=0.2)
    print(len(test), len(train), len(result), hipotesis)

    return hipotesis


def get_hipotesis_find_s(result, attrs, concepto, condicion_cumplida):
    hipotesis = ["∅"] * len(attrs)

    for item in result:
        if item[concepto] == condicion_cumplida:
            for i, h in enumerate(hipotesis):
                if h == "∅":
                    hipotesis[i] = item[attrs[i]]
                elif h == item[attrs[i]]:
                    continue
                else:
                    hipotesis[i] = "?"
    return hipotesis


def filter_data_prestamo(data, attrs, concepto, age):
    result = []
    for row in data:
        if int(row["Edad"]) == age:
            personal_data = {}
            for attr in attrs:
                personal_data[attr] = row[attr]
            result.append(
                {
                    **personal_data,
                    concepto: row[concepto],
                }
            )
    return result
