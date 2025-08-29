import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from tp_1.find_s import part_1_2
from tp_1.part_3 import part_3
from utils.helpers import cargar_csv

def main():
    #print(part_1_2())
    print(part_3())
    
if __name__ == "__main__":
    main()