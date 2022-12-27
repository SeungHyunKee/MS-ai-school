# 단층 퍼셉트론 이용하면 and nanad or 게이트 구현가능

# and 게이트 구현
# and 게이트를 만족하는 두개의 가중치와 편향값에는 무엇이있는가?
# w1, w2, b 라고하면 (w=가중치, b=편)
# 0.5 0.2 0.1 -> 결과 구해진 수치 [0.5, 0.5, -0.7]

def and_gate(x1, x2):
    w1 = 0.5
    w2 = 0.5
    b = -0.7

    # x1w1 + x2w2 + b
    result = x1*w1 + x2*w2 + b
    print(result)

    if result <= 0:
        return 0
    else:
        return 1
    
print(and_gate(1,1))




# 단층퍼셉트론 NAND 게이트 구현
# 두개 입력값 1일때만 0, 나머지경우는 1

def nand_gate(x1, x2):
    w1 = -0.5
    w2 = -0.5
    b = 0.7

    # x1w1 + x2w2 + b
    result = x1*w1 + x2*w2 + b
    # print(result)

    if result <= 0:
        return 0
    else:
        return 1

print(nand_gate(0,0))



def or_gate(x1, x2):
    w1 = 0.5
    w2 = 0.5
    b = -0.4

    result = x1*w1 + x2*w2 + b

    if result <= 0:
        return 0 
    else:
        return 1
print(or_gate(0,0))
 
    