def get_hipotesis_find_s(result, attrs, concepto, condicion_cumplida):
    hipotesis = ["∅"] * len(attrs)

    for item in result:
        if item[concepto] == condicion_cumplida:
            for index, h in enumerate(hipotesis):
                if h == "∅":
                    hipotesis[index] = item[attrs[index]]
                elif h == item[attrs[index]]:
                    continue
                else:
                    hipotesis[index] = "?"
    return hipotesis


def filter_data_prestamo(data, attrs, concepto, ages):
    result = []
    for row in data:
        if int(row["Edad"]) in ages:

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


def evaluate_find_s(test, hipotesis, attrs, prediction_column="prediction"):
    result = []
    for row in test:
        correct = True
        for index, attr in enumerate(attrs):
            if hipotesis[index] == "?" or hipotesis[index] == row[attr]:
                continue
            else:
                correct = False
                break

        row[prediction_column] = 1 if correct else 0
        result.append(row)

    return result
