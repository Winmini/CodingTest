import sys
from itertools import permutations

T = int(input())
answer = list(permutations([str(i) for i in range(1, 10)], 3))
for _ in range(T):
    num, strike, ball = sys.stdin.readline().split()
    strike = int(strike)
    ball = int(ball)
    tmp = []
    for i in answer:
        if strike == ball == 0:
            if num[0] not in i and num[1] not in i and num[2] not in i:
                tmp.append(i)
        if strike == 1 and ball == 0:
            if num[0] == i[0] and num[1] not in i and num[2] not in i:
                tmp.append(i)
            elif num[0] not in i[0] and num[1] == i[1] and num[2] not in i:
                tmp.append(i)
            elif num[0] not in i[0] and num[1] not in i[1] and num[2] == i[2]:
                tmp.append(i)
        if strike == 2 and ball == 0:
            if num[0] == i[0] and num[1] == i[1] and num[2] not in i:
                tmp.append(i)
            elif num[0] == i[0] and num[1] not in i and num[2] == i[2]:
                tmp.append(i)
            elif num[0] not in i and num[1] == i[1] and num[2] == i[2]:
                tmp.append(i)
        if strike == 3:
            if num[0] == i[0] and num[1] == i[1] and num[2] == i[2]:
                tmp.append(i)
        if strike == 0 and ball == 1:
            if num[0] not in i and num[1] not in i and num[2] in i and num[2] != i[2]:
                tmp.append(i)
            elif num[0] not in i and num[1] in i and num[1] != i[1] and num[2] not in i:
                tmp.append(i)
            elif num[0] in i and num[0] != i[0] and num[1] not in i and num[2] not in i:
                tmp.append(i)
        if strike == 0 and ball == 2:
            if num[0] not in i and num[1] in i and num[1] != i[1] and num[2] in i and num[2] != i[2]:
                tmp.append(i)
            elif num[0] in i and num[0] != i[0] and num[1] in i and num[1] != i[1] and num[2] not in i:
                tmp.append(i)
            elif num[0] in i and num[0] != i[0] and num[1] not in i and num[2] in i and num[2] != i[2]:
                tmp.append(i)
        if strike == 0 and ball == 3:
            if num[0] in i and num[1] in i and num[2] in i and num[0] != i[0] and num[1] != i[1] and num[2] != i[2]:
                tmp.append(i)
        if strike == 1 and ball == 2:
            if num[0] == i[0] and num[1] == i[2] and num[2] == i[1]:
                tmp.append(i)
            elif num[0] == i[1] and num[1] == i[0] and num[2] == i[2]:
                tmp.append(i)
            elif num[0] == i[2] and num[1] == i[1] and num[2] == i[0]:
                tmp.append(i)
        if strike == 1 and ball == 1:
            if num[0] == i[0] and num[1] in i and num[1] != i[1] and num[2] not in i:
                tmp.append(i)
            elif num[0] == i[0] and num[1] not in i and num[2] in i and num[2] != i[2]:
                tmp.append(i)
            elif num[1] == i[1] and num[0] == i[2] and num[2] not in i:
                tmp.append(i)
            elif num[1] == i[1] and num[2] == i[0] and num[0] not in i:
                tmp.append(i)
            elif num[2] == i[2] and num[1] == i[0] and num[0] not in i:
                tmp.append(i)
            elif num[2] == i[2] and num[0] == i[1] and num[1] not in i:
                tmp.append(i)
    answer = tmp[:]
print(len(answer))




#####################단축코드######################
import sysimport sys
from itertools import permutations

T = int(input())
answer = list(permutations([str(i) for i in range(1, 10)], 3))
for _ in range(T):
    num, strike, ball = sys.stdin.readline().split()
    tmp = []
    for i in answer:
        s = 0
        b = 0
        for n in range(3):
            if num[n] == i[n]:
                s += 1
            elif num[n] in i:
                b += 1
        if strike == str(s) and ball == str(b):
            tmp.append(i)
    answer = tmp[:]
print(len(answer))