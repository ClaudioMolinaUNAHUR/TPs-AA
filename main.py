import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from tp_1.find_s import run_find_s
from utils.helpers import cargar_csv

def main():
    print(run_find_s())
    
if __name__ == "__main__":
    main()