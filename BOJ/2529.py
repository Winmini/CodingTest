import sys
from itertools import permutations
INF = int(1e9)


k = int(input())
op = sys.stdin.readline().split()
num = range(10)
x = list(permutations(num, k + 1))

answer = []
for p in x:
    tmp = 0
    for i in range(k):
        if op[i] == '>':
            if p[i] > p[i+1]:
                tmp += 1
            else:
                break
        else:
            if p[i] < p[i+1]:
                tmp += 1
            else:
                break
    if tmp == k:
        answer.append(p)
for i in answer[-1]:
    print(str(i), end='')
print()
for i in answer[0]:
    print(str(i), end='')