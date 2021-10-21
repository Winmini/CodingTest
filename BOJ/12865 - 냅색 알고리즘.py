import sys


N, K = [int(i) for i in sys.stdin.readline().split()]

things = [[0, 0]]
bag = [[0]*(K+1) for _ in range(N+1)]

for i in range(N):
    things.append([int(i) for i in sys.stdin.readline().split()])

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = things[i][0]
        value = things[i][1]
        if j < weight:
            bag[i][j] = bag[i-1][j]
        else:
            bag[i][j] = max(bag[i-1][j], bag[i-1][j-weight]+value)
print(bag[N][K])