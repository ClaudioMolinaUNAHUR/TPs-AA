from utils.helpers import (
    cargar_csv,
    split_test_data,
    confusion_matrix,
    f1_score,
    precision_score,
    accuracy_score,
    recall_score,
    filter_data_prestamo,
    save_json
)
from tp_2.addons.functions import id3, evaluate_id3


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
    # print(tree)
    evaluated = []
    print("test: ", len(test))
    print("train: ", len(train))
    print("total: ", len(result))
    for row in test:
        clase = evaluate_id3(row, tree)
        row[prediction_column] = 1 if condicion_cumplida == clase else 0
        evaluated.append(row)

    confusion_matrix_result = confusion_matrix(
        evaluated, concepto, prediction_column, condicion_cumplida
    )

    tp = confusion_matrix_result["tp"]
    tn = confusion_matrix_result["tn"]
    fp = confusion_matrix_result["fp"]
    fn = confusion_matrix_result["fn"]

    accuracy = accuracy_score(tp, tn, fp, fn)
    recall = recall_score(tp, fn)
    precision = precision_score(tp, fp)
    f1 = f1_score(precision, recall)
    save_json("./tp_2/tree.json", tree)
    return {
        "accuracy": accuracy,
        "f1": f1,
        "confusion_matrix": confusion_matrix_result,
    }


{
    "Préstamos previos impagos": {
        "SI": "RECHAZADO",
        "NO": {
            "Estado de vivienda": {
                "OTRO": {
                    "Mayor nivel educativo": {
                        "SECUNDARIO": "OTORGADO",
                        "TERCIARIO": {
                            "Destino de los fondos": {
                                "VIVIENDA": "RECHAZADO",
                                "EDUCACION": "OTORGADO",
                                "PERSONAL": "OTORGADO",
                            },
                            "metrics": {
                                "IG": 1.0,
                                "Class": {"RECHAZADO": 2, "OTORGADO": 2},
                            },
                        },
                        "UNIVERSITARIO": "RECHAZADO",
                    },
                    "metrics": {
                        "IG": 0.41379956460568024,
                        "Class": {"RECHAZADO": 4, "OTORGADO": 3},
                    },
                },
                "PROPIETARIO": {
                    "Mayor nivel educativo": {
                        "DOCTORADO": "OTORGADO",
                        "UNIVERSITARIO": "RECHAZADO",
                        "TERCIARIO": {
                            "Destino de los fondos": {
                                "EDUCACION": {
                                    "Sexo": {"MASCULINO": "OTORGADO"},
                                    "metrics": {
                                        "IG": 0.0,
                                        "Class": {"OTORGADO": 1, "RECHAZADO": 1},
                                    },
                                },
                                "EMPRESA": "RECHAZADO",
                                "SALUD": "RECHAZADO",
                                "PERSONAL": "RECHAZADO",
                            },
                            "metrics": {
                                "IG": 0.3059584928680418,
                                "Class": {"OTORGADO": 1, "RECHAZADO": 6},
                            },
                        },
                        "MAESTRíA": "RECHAZADO",
                        "SECUNDARIO": {
                            "Destino de los fondos": {
                                "PERSONAL": "RECHAZADO",
                                "EDUCACION": "RECHAZADO",
                                "SALUD": {
                                    "Sexo": {"MASCULINO": "RECHAZADO"},
                                    "metrics": {
                                        "IG": 0.0,
                                        "Class": {"RECHAZADO": 2, "OTORGADO": 1},
                                    },
                                },
                                "VIVIENDA": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.2516291673878229,
                                        "Class": {"OTORGADO": 1, "RECHAZADO": 2},
                                    },
                                },
                                "EMPRESA": "RECHAZADO",
                            },
                            "metrics": {
                                "IG": 0.19920350542916282,
                                "Class": {"OTORGADO": 2, "RECHAZADO": 14},
                            },
                        },
                    },
                    "metrics": {
                        "IG": 0.14378231935937996,
                        "Class": {"OTORGADO": 4, "RECHAZADO": 29},
                    },
                },
                "INQUILINO": {
                    "Mayor nivel educativo": {
                        "DOCTORADO": {
                            "Destino de los fondos": {
                                "EDUCACION": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "OTORGADO",
                                    },
                                    "metrics": {
                                        "IG": 0.9182958340544896,
                                        "Class": {"OTORGADO": 1, "RECHAZADO": 2},
                                    },
                                },
                                "PERSONAL": "RECHAZADO",
                                "SALUD": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.024757614058220967,
                                        "Class": {"RECHAZADO": 6, "OTORGADO": 3},
                                    },
                                },
                                "VIVIENDA": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "OTORGADO",
                                    },
                                    "metrics": {
                                        "IG": 0.31127812445913283,
                                        "Class": {"OTORGADO": 3, "RECHAZADO": 1},
                                    },
                                },
                                "EMPRESA": "RECHAZADO",
                            },
                            "metrics": {
                                "IG": 0.22083493005097066,
                                "Class": {"OTORGADO": 7, "RECHAZADO": 13},
                            },
                        },
                        "UNIVERSITARIO": {
                            "Destino de los fondos": {
                                "EDUCACION": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.8112781244591328,
                                        "Class": {"OTORGADO": 2, "RECHAZADO": 6},
                                    },
                                },
                                "DEUDAS": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.003585078590305768,
                                        "Class": {"OTORGADO": 8, "RECHAZADO": 9},
                                    },
                                },
                                "PERSONAL": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.19087450462110933,
                                        "Class": {"RECHAZADO": 5, "OTORGADO": 1},
                                    },
                                },
                                "SALUD": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.020720839623907805,
                                        "Class": {"OTORGADO": 6, "RECHAZADO": 6},
                                    },
                                },
                                "VIVIENDA": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "OTORGADO",
                                    },
                                    "metrics": {
                                        "IG": 0.2516291673878229,
                                        "Class": {"OTORGADO": 2, "RECHAZADO": 1},
                                    },
                                },
                                "EMPRESA": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.04879494069539858,
                                        "Class": {"RECHAZADO": 5, "OTORGADO": 3},
                                    },
                                },
                            },
                            "metrics": {
                                "IG": 0.05404013272973007,
                                "Class": {"OTORGADO": 22, "RECHAZADO": 32},
                            },
                        },
                        "TERCIARIO": {
                            "Destino de los fondos": {
                                "EDUCACION": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.019663704265785675,
                                        "Class": {"RECHAZADO": 13, "OTORGADO": 10},
                                    },
                                },
                                "DEUDAS": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "OTORGADO",
                                    },
                                    "metrics": {
                                        "IG": 0.007947308532810338,
                                        "Class": {"OTORGADO": 10, "RECHAZADO": 10},
                                    },
                                },
                                "PERSONAL": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.008923940161777777,
                                        "Class": {"RECHAZADO": 9, "OTORGADO": 9},
                                    },
                                },
                                "SALUD": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.006900300371591506,
                                        "Class": {"OTORGADO": 12, "RECHAZADO": 14},
                                    },
                                },
                                "VIVIENDA": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "OTORGADO",
                                    },
                                    "metrics": {
                                        "IG": 0.03276539733096595,
                                        "Class": {"OTORGADO": 7, "RECHAZADO": 4},
                                    },
                                },
                                "EMPRESA": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.035879877173714214,
                                        "Class": {"RECHAZADO": 9, "OTORGADO": 7},
                                    },
                                },
                            },
                            "metrics": {
                                "IG": 0.009398615057378046,
                                "Class": {"OTORGADO": 55, "RECHAZADO": 59},
                            },
                        },
                        "MAESTRíA": {
                            "Destino de los fondos": {
                                "EDUCACION": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "OTORGADO",
                                    },
                                    "metrics": {
                                        "IG": 0.12255624891826566,
                                        "Class": {"OTORGADO": 3, "RECHAZADO": 1},
                                    },
                                },
                                "DEUDAS": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.024757614058220967,
                                        "Class": {"OTORGADO": 3, "RECHAZADO": 6},
                                    },
                                },
                                "PERSONAL": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.12808527889139454,
                                        "Class": {"OTORGADO": 3, "RECHAZADO": 4},
                                    },
                                },
                                "SALUD": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "OTORGADO",
                                    },
                                    "metrics": {
                                        "IG": 0.12451124978365313,
                                        "Class": {"OTORGADO": 5, "RECHAZADO": 5},
                                    },
                                },
                                "VIVIENDA": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "OTORGADO",
                                    },
                                    "metrics": {
                                        "IG": 0.17095059445466854,
                                        "Class": {"OTORGADO": 3, "RECHAZADO": 2},
                                    },
                                },
                                "EMPRESA": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.01997309402197489,
                                        "Class": {"OTORGADO": 3, "RECHAZADO": 2},
                                    },
                                },
                            },
                            "metrics": {
                                "IG": 0.047103052472165285,
                                "Class": {"OTORGADO": 20, "RECHAZADO": 20},
                            },
                        },
                        "SECUNDARIO": {
                            "Destino de los fondos": {
                                "EDUCACION": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "OTORGADO",
                                    },
                                    "metrics": {
                                        "IG": 0.0004894691870231949,
                                        "Class": {"OTORGADO": 9, "RECHAZADO": 5},
                                    },
                                },
                                "DEUDAS": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "OTORGADO",
                                    },
                                    "metrics": {
                                        "IG": 0.03170514719803608,
                                        "Class": {"OTORGADO": 10, "RECHAZADO": 5},
                                    },
                                },
                                "PERSONAL": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "OTORGADO",
                                    },
                                    "metrics": {
                                        "IG": 0.05976709447343753,
                                        "Class": {"OTORGADO": 12, "RECHAZADO": 9},
                                    },
                                },
                                "SALUD": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "OTORGADO",
                                    },
                                    "metrics": {
                                        "IG": 0.09461325594033099,
                                        "Class": {"OTORGADO": 14, "RECHAZADO": 14},
                                    },
                                },
                                "VIVIENDA": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "OTORGADO",
                                    },
                                    "metrics": {
                                        "IG": 0.001881577131005896,
                                        "Class": {"OTORGADO": 9, "RECHAZADO": 7},
                                    },
                                },
                                "EMPRESA": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "OTORGADO",
                                    },
                                    "metrics": {
                                        "IG": 0.03494091395622845,
                                        "Class": {"RECHAZADO": 7, "OTORGADO": 6},
                                    },
                                },
                            },
                            "metrics": {
                                "IG": 0.013700715709506595,
                                "Class": {"OTORGADO": 60, "RECHAZADO": 47},
                            },
                        },
                    },
                    "metrics": {
                        "IG": 0.01134357592630153,
                        "Class": {"OTORGADO": 164, "RECHAZADO": 171},
                    },
                },
                "HIPOTECA": {
                    "Destino de los fondos": {
                        "EDUCACION": {
                            "Mayor nivel educativo": {
                                "DOCTORADO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.2516291673878229,
                                        "Class": {"RECHAZADO": 2, "OTORGADO": 1},
                                    },
                                },
                                "TERCIARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.14653542331781932,
                                        "Class": {"RECHAZADO": 10, "OTORGADO": 2},
                                    },
                                },
                                "UNIVERSITARIO": "RECHAZADO",
                                "MAESTRíA": "OTORGADO",
                                "SECUNDARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.01653216923776102,
                                        "Class": {"RECHAZADO": 13, "OTORGADO": 1},
                                    },
                                },
                            },
                            "metrics": {
                                "IG": 0.1362732882382806,
                                "Class": {"RECHAZADO": 28, "OTORGADO": 5},
                            },
                        },
                        "DEUDAS": {
                            "Mayor nivel educativo": {
                                "DOCTORADO": "OTORGADO",
                                "UNIVERSITARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.12255624891826566,
                                        "Class": {"RECHAZADO": 3, "OTORGADO": 1},
                                    },
                                },
                                "TERCIARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.030028265235621965,
                                        "Class": {"RECHAZADO": 11, "OTORGADO": 7},
                                    },
                                },
                                "MAESTRíA": "RECHAZADO",
                                "SECUNDARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "OTORGADO",
                                    },
                                    "metrics": {
                                        "IG": 0.03494091395622845,
                                        "Class": {"RECHAZADO": 7, "OTORGADO": 6},
                                    },
                                },
                            },
                            "metrics": {
                                "IG": 0.06745764439551727,
                                "Class": {"RECHAZADO": 22, "OTORGADO": 15},
                            },
                        },
                        "PERSONAL": {
                            "Mayor nivel educativo": {
                                "DOCTORADO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "OTORGADO",
                                    },
                                    "metrics": {
                                        "IG": 0.31127812445913283,
                                        "Class": {"RECHAZADO": 2, "OTORGADO": 2},
                                    },
                                },
                                "UNIVERSITARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "OTORGADO",
                                    },
                                    "metrics": {
                                        "IG": 1.0,
                                        "Class": {"RECHAZADO": 1, "OTORGADO": 1},
                                    },
                                },
                                "TERCIARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.0059777114237739015,
                                        "Class": {"RECHAZADO": 5, "OTORGADO": 2},
                                    },
                                },
                                "MAESTRíA": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.3219280948873623,
                                        "Class": {"OTORGADO": 2, "RECHAZADO": 3},
                                    },
                                },
                                "SECUNDARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.11774369689072062,
                                        "Class": {"OTORGADO": 2, "RECHAZADO": 8},
                                    },
                                },
                            },
                            "metrics": {
                                "IG": 0.04464686243180693,
                                "Class": {"RECHAZADO": 19, "OTORGADO": 9},
                            },
                        },
                        "SALUD": {
                            "Mayor nivel educativo": {
                                "DOCTORADO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.2516291673878229,
                                        "Class": {"RECHAZADO": 2, "OTORGADO": 1},
                                    },
                                },
                                "TERCIARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.003131748843799631,
                                        "Class": {"RECHAZADO": 16, "OTORGADO": 7},
                                    },
                                },
                                "UNIVERSITARIO": {
                                    "Sexo": {
                                        "MASCULINO": "OTORGADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.12451124978365313,
                                        "Class": {"OTORGADO": 4, "RECHAZADO": 6},
                                    },
                                },
                                "MAESTRíA": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.17095059445466865,
                                        "Class": {"RECHAZADO": 4, "OTORGADO": 1},
                                    },
                                },
                                "SECUNDARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.008986624929939513,
                                        "Class": {"OTORGADO": 6, "RECHAZADO": 9},
                                    },
                                },
                            },
                            "metrics": {
                                "IG": 0.012906160333062466,
                                "Class": {"OTORGADO": 19, "RECHAZADO": 37},
                            },
                        },
                        "VIVIENDA": {
                            "Mayor nivel educativo": {
                                "SECUNDARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.17498878917582283,
                                        "Class": {"RECHAZADO": 8, "OTORGADO": 4},
                                    },
                                },
                                "DOCTORADO": "RECHAZADO",
                                "TERCIARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.09265128879158102,
                                        "Class": {"RECHAZADO": 13, "OTORGADO": 1},
                                    },
                                },
                                "UNIVERSITARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "OTORGADO",
                                    },
                                    "metrics": {
                                        "IG": 0.2516291673878229,
                                        "Class": {"OTORGADO": 1, "RECHAZADO": 2},
                                    },
                                },
                            },
                            "metrics": {
                                "IG": 0.09684567062930571,
                                "Class": {"RECHAZADO": 25, "OTORGADO": 6},
                            },
                        },
                        "EMPRESA": {
                            "Mayor nivel educativo": {
                                "DOCTORADO": "RECHAZADO",
                                "UNIVERSITARIO": "RECHAZADO",
                                "TERCIARIO": {
                                    "Sexo": {
                                        "MASCULINO": "RECHAZADO",
                                        "FEMENINO": "RECHAZADO",
                                    },
                                    "metrics": {
                                        "IG": 0.025850761940059863,
                                        "Class": {"RECHAZADO": 7, "OTORGADO": 1},
                                    },
                                },
                                "MAESTRíA": "RECHAZADO",
                                "SECUNDARIO": {
                                    "Sexo": {"MASCULINO": "RECHAZADO"},
                                    "metrics": {
                                        "IG": 0.0,
                                        "Class": {"RECHAZADO": 9, "OTORGADO": 5},
                                    },
                                },
                            },
                            "metrics": {
                                "IG": 0.17470804127314637,
                                "Class": {"RECHAZADO": 36, "OTORGADO": 6},
                            },
                        },
                    },
                    "metrics": {
                        "IG": 0.039226764008684634,
                        "Class": {"OTORGADO": 60, "RECHAZADO": 167},
                    },
                },
            },
            "metrics": {
                "IG": 0.04948299378807053,
                "Class": {"OTORGADO": 231, "RECHAZADO": 371},
            },
        },
    },
    "IG": 0.21988131535432698,
    "Class": {"OTORGADO": 231, "RECHAZADO": 909},
}
