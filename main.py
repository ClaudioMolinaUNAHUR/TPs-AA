import os
import sys
from utils.helpers import like_json
from tp_1.part_1_2 import tp1_part_1_2
from tp_1.part_3 import tp1_part_3
from tp_2.part_1 import tp2_part_1
from tp_2.part_2 import tp2_part_2
from tp_3.part_1 import tp3_part_1 
from tp_3.part_2 import tp3_part_2
from tp_4.part_1 import tp4_part_1
from tp_4.part_2 import tp4_part_2
import json


sys.path.append(os.path.abspath(os.path.dirname(__file__)))


def main():
    # result_1 = tp1_part_1_2()
    # result_2 = tp1_part_3()
    
    
    # print("Resultado 1_2: ", like_json(result_1))
    # print("Resultado 3: ", like_json(result_2))
    
    # tp_2_result_1 = tp2_part_1()    
    # tp_2_result_2 = tp2_part_2()  
    # print("Resultado 1: ", like_json(tp_2_result_1))
    # print("Resultado 2: ", like_json(tp_2_result_2))

    # tp_3_result_1 = tp3_part_1()
    # print("Resultado Ejercicio 1:\n", like_json(tp_3_result_1))
    # tp_3_result_3 = tp3_part_2()
    # print("Resultado Ejercicio 2:\n", like_json(tp_3_result_3))
    
    tp_4_result_1 = tp4_part_1()
    print("Resultado Ejercicio 1:\n", like_json(tp_4_result_1))
    tp_4_result_2 = tp4_part_2()
    print("Resultado Ejercicio 2:\n", like_json(tp_4_result_2))



if __name__ == "__main__":
    main()
