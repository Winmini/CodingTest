from itertools import combinations
import sys


N, M = [int(i) for i in sys.stdin.readline().split()]
board = []
for _ in range(N):
    board.append([int(i) for i in sys.stdin.readline().split()])

house = []
kfc = []

for idx, block in enumerate(board):
    for idy, i in enumerate(block):
        if i == 1:
            house.append([idx, idy])
        elif i == 2:
            kfc.append([idx, idy])

t_kfc = list(combinations(kfc, M))
answer = 1000000
for i in t_kfc:
    kfc = i
    tmp0 = 0
    for x, y in house:
        tmp = 1000000
        for k in kfc:
            tmp = min(tmp, abs(x - k[0]) + abs(y - k[1]))
        tmp0 += tmp
    answer = min(answer, tmp0)
print(answer)