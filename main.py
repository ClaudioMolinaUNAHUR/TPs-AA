import os
import sys
from tp_1.part_1_2 import part_1_2
from tp_1.part_3 import part_3
from tp_2.part_1 import tp2_part_1
from tp_2.part_2 import tp2_part_2
import json


sys.path.append(os.path.abspath(os.path.dirname(__file__)))

def like_json(data):
    return json.dumps(data, indent=2, ensure_ascii=False)

def main():
    # result_1 = part_1_2()
    # result_2 = part_3()
    
    
    # print("Resultado 1_2: ", like_json(result_1))
    # print("Resultado 3: ", like_json(result_2))
    
    tp_2_result_1 = tp2_part_1()    
    tp_2_result_2 = tp2_part_2()  
    print("Resultado 1: ", like_json(tp_2_result_1))
    print("Resultado 2: ", like_json(tp_2_result_2))

if __name__ == "__main__":
    main()
