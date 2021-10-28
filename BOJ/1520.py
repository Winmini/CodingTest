import sys
sys.setrecursionlimit(10**6)


def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    if x == M-1 and y == N-1:
        return 1
    dp[x][y] = 0
    for i in range(4):
        cur_x = x + dir_x[i]
        cur_y = y + dir_y[i]
        if 0 <= cur_x < M and 0 <= cur_y < N:
            if board[cur_x][cur_y] < board[x][y]:
                dp[x][y] += dfs(cur_x, cur_y)
    return dp[x][y]


dir_x = [0, 1, -1, 0]
dir_y = [-1, 0, 0, 1]

M, N = [int(i) for i in sys.stdin.readline().split()]
board = []
dp = [[-1] * (N+1) for _ in range(M+1)]
for _ in range(M):
    board.append([int(i) for i in sys.stdin.readline().split()])
print(dfs(0, 0))