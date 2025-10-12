import os
import sys
from utils.helpers import like_json
from tp_1.part_1_2 import tp1_part_1_2
from tp_1.part_3 import tp1_part_3
from tp_2.part_1 import tp2_part_1
from tp_2.part_2 import tp2_part_2


sys.path.append(os.path.abspath(os.path.dirname(__file__)))


def main():
    tp1_result_1 = tp1_part_1_2()
    tp1_result_2 = tp1_part_3()
    print("Resultado FIND-S: ", like_json(tp1_result_1))
    print("Resultado NAIVE BAYES: ", like_json(tp1_result_2))

    tp_2_result_1 = tp2_part_1()
    tp_2_result_2 = tp2_part_2()
    print("Resultado ID3: ", like_json(tp_2_result_1))
    print("Resultado RANDOM FOREST: ", like_json(tp_2_result_2))


if __name__ == "__main__":
    main()
