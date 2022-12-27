# 다중 퍼습트론을 이용한 XOR_gate 구현

import numpy as np
# from ex07 import *
# import ex07

# ex07.or_gate

def and_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7

    temp = np.sum(w*x) + b
    if temp <= 0: 
        return 0
    else:
        return 1

 
def nand_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7

    temp = np.sum(w*x) + b
    if temp <= 0: 
        return 0
    else:
        return 1


def or_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2

    temp = np.sum(w*x) + b
    if temp <= 0: 
        return 0
    else:
        return 1



def xor_gate(x1, x2):
    s1 = nand_gate(x1, x2)
    s2 = or_gate(x1, x2)
    y = and_gate(s1, s2)

    return y

    # 기존함수 호출사용
    # s1 = ex07.nand_gate(x1, x2)