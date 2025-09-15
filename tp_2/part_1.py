from utils.helpers import (
    cargar_csv,
    split_test_data,
    confusion_matrix,
    f1_score,
    precision_score,
    accuracy_score,
    recall_score,
    filter_data_prestamo,
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

    return {
        "tree": tree,
        "accuracy": accuracy,
        "f1": f1,
        "confusion_matrix": confusion_matrix_result,
    }


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
