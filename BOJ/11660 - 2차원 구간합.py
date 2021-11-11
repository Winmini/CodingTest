import sys

N, M = [int(i) for i in sys.stdin.readline().split()]
board = []
for _ in range(N):
    board.append([int(i) for i in sys.stdin.readline().split()])
pSum = [[0] * (N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        pSum[i+1][j+1] = pSum[i+1][j] + pSum[i][j+1] - pSum[i][j] + board[i][j]

for _ in range(M):
    x1, y1, x2, y2 = [int(i) for i in sys.stdin.readline().split()]
    print(pSum[x2][y2] - pSum[x1-1][y2] - pSum[x2][y1-1] + pSum[x1-1][y1-1])