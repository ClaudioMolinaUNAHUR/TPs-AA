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


def discrete_naive_bayes(test_row, train, attrs, concepto_column, condicion_cumplida):
    class_rows = {}
    N = len(train)
    pi = {}
    theta = {}
    laplace = 1
    types_vals_attr = {}

    for attr in attrs:
        value = test_row[attr]
        if value not in theta:
            theta[value] = {"attr": attr}

    for row in train:
        if row[concepto_column] not in class_rows:
            class_rows[row[concepto_column]] = []
            pi[row[concepto_column]] = 0

        class_rows[row[concepto_column]].append(row)

        for attr in attrs:
            value_row = row[attr]
            if attr not in types_vals_attr:
                types_vals_attr[attr] = set()
            types_vals_attr[attr].add(value_row)

            for value_t in theta:
                if value_t == value_row and theta[value_t]["attr"] == attr:
                    if row[concepto_column] not in theta[value_t]:
                        theta[value_t][row[concepto_column]] = 0

                    theta[value_t][row[concepto_column]] += 1
                    break

    # print(pi, "% de cada")
    # print(theta)
    total_probability = 0
    probability = {}
    for K in pi:
        quantity_items_in_class = len(class_rows[K])
        numerador_pi = quantity_items_in_class + laplace

        quantity_Ks = len(class_rows)
        denominador_pi = N + laplace * quantity_Ks

        pi[K] = numerador_pi / denominador_pi

        producto = 1
        for value in theta:
            quantity_value_theta = theta[value].get(K, 0)
            numerador_theta = quantity_value_theta + laplace

            quantity_values_from_attr = len(types_vals_attr[theta[value].get("attr")])
            N_register_class = len(class_rows[K])

            denominador_theta = N_register_class + laplace * quantity_values_from_attr

            producto *= numerador_theta / denominador_theta

        # print(producto, classes, "PRODUCTO")
        probability[K] = pi[K] * producto
        total_probability += probability[K]
    # print(pi)
    accept = 0
    reject = 0
    for K in probability:
        if K == condicion_cumplida:
            accept = probability[K] / total_probability
        else:
            reject = probability[K] / total_probability

    # print(accept, reject)
    return accept if accept > reject else abs(reject - 1)
