# ind
# 50 años "Edad"
# sexo "Sexo"
# educacion "Mayor nivel educativo"
# vivienda "Estado de vivienda"
# posee prestamo "Préstamos previos impagos"

# dep
# estado "Estado"
import numpy as np
from utils.helpers import accuracy_score, split_test_data, cargar_csv, confusion_matrix, specificity_score,recall_score,precision_score, f1_score, TPR_score, FPR_score


def part_3():
    file_path = "./tp_1/Préstamo.csv"
    data = cargar_csv(file_path, "latin-1")

    attrs = [
        "Sexo",
        "Mayor nivel educativo",
        "Estado de vivienda",
        "Préstamos previos impagos",
        "Destino de los fondos"
    ]
    concepto = "Estado"
    condicion_cumplida = "OTORGADO"
    prediction_column = "prediction"

   #print(data)


   

    result = filter_data_prestamo(data, attrs, concepto, [40,45] )


    test, train = split_test_data(result, test_size=0.25)
    hipotesis = get_hipotesis_find_s(train, attrs, concepto, condicion_cumplida)


    evaluated = evaluate_find_s(test, hipotesis,attrs,prediction_column)
    confusion_matrix_result = confusion_matrix(evaluated, concepto, prediction_column, condicion_cumplida)
    #print(confusion_matrix_result)

    tp=confusion_matrix_result["tp"]
    tn=confusion_matrix_result["tn"]
    fp=confusion_matrix_result["fp"]
    fn=confusion_matrix_result["fn"]
    accuracy = accuracy_score(tp, tn, fp, fn)
    specificity = specificity_score(tn, fp) 
    recall = recall_score(tp,fn)
    precision= precision_score(tp,fp)
    f1 = f1_score(precision, recall)
    TPR = TPR_score(tp, fn)
    FPR= FPR_score(fp, tn)

   
    #print(len(test), len(train), len(result), hipotesis)

    return hipotesis

# TODO: poner print para el conj de prueba

def evaluate_find_s(test, hipotesis,attrs,prediction_column = "prediction"):
    result = []
    for row in test:  
        correct = True
        for index,attr in enumerate(attrs):
            #print(hipotesis[index], row[attr])
            if hipotesis[index] == "?" or hipotesis[index] == row[attr]:
                #print(row)
                continue
            else:
                correct = False
                break
      
        row[prediction_column] = 1 if correct else 0
        result.append(row)
        
    #print(len(result))

    return result
        
        #print(index, row)

    
       
            


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
    print(result)
    return result
