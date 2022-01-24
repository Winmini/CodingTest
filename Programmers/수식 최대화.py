import re
from itertools import permutations


def solution(expression):
    answer = 0
    num = re.split("[*+-]", expression)
    op = []
    order = ["*", "+", "-"]
    for i in expression:
        if i == "*" or i == "+" or i == "-":
            op.append(i)
        
    for i in permutations([0,1,2], 3):
        t_num = num[:]
        t_op = op[:]
        for k in range(3):
            while True:
                if not order[i[k]] in t_op:
                    break
                for idx, o in enumerate(t_op):
                    if o == order[i[k]]:
                        t_num[idx] = str(eval(t_num[idx] + o + t_num[idx + 1]))
                        t_num.pop(idx+1)
                        t_op.pop(idx)
                        break
        answer = max(answer, abs(int(t_num[0])))
        
    return answer