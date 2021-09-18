import sys


a = int(input())
w = [0] * (a + 1)
w[1] = int(input())
tmp = [[0 for i in range(502)] for j in range(502)]
tmp[1][0] = w[1]
if a == 1:
    print(w[1])
else:
    for i in range(2, a + 1):
        k = [int(i) for i in sys.stdin.readline().split()]
        tmp[i][0] = tmp[i-1][0] + k[0]
        for j in range(1, i):
            tmp[i][j] = max(tmp[i-1][j-1], tmp[i-1][j]) + k[j]
        tmp[i][i] = tmp[i-1][i-1] + k[i-1]
        w[i] = max(tmp[i])
    print(w[a])