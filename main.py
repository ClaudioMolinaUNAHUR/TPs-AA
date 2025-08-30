import os
import sys
from tp_1.part_1_2 import part_1_2
from tp_1.part_3 import part_3
import json


sys.path.append(os.path.abspath(os.path.dirname(__file__)))

def likeJson(data):
    return json.dumps(data, indent=2, ensure_ascii=False)

def main():
    result_1 = part_1_2()
    result_2 = part_3()
    
    ## print("Resultado 1_2: ", likeJson(result_1))
    print("Resultado 3: ", likeJson(result_2))


if __name__ == "__main__":
    main()
