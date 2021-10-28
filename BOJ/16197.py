from collections import deque
import sys


dir_x = [0, 1, -1, 0]
dir_y = [-1, 0, 0, 1]
N, M = [int(i) for i in sys.stdin.readline().split()]
visit = [[[[False for _ in range(25)] for _ in range(25)] for _ in range(25)] for _ in range(25)]
coin = []
board = [['x'] * (M + 2)]
for _ in range(N):
    board.append(['x'] + list(input()) + ['x'])
board.append(['x'] * (M + 2))
for i in range(N + 2):
    for j in range(M + 2):
        if board[i][j] == 'o':
            coin.append([i, j])
q = deque([[coin[0], coin[1], [0]]])
answer = 0
while q:
    coin1, coin2, n = q.popleft()
    if n[0] > 9:
        continue
    coin1_x, coin1_y = coin1
    coin2_x, coin2_y = coin2
    visit[coin1_x][coin1_y][coin2_x][coin2_y] = True
    for i in range(4):
        c1_x = coin1_x + dir_x[i]
        c1_y = coin1_y + dir_y[i]
        c2_x = coin2_x + dir_x[i]
        c2_y = coin2_y + dir_y[i]
        if board[c1_x][c1_y] == 'x' and board[c2_x][c2_y] == 'x':
            continue
        if board[c1_x][c1_y] == '#' and board[c2_x][c2_y] == '#':
            continue
        if visit[c1_x][c1_y][c2_x][c2_y]:
            continue
        if board[c1_x][c1_y] == 'x' and board[c2_x][c2_y] != 'x':
            print(n[0] + 1)
            sys.exit(0)
        elif board[c2_x][c2_y] == 'x' and board[c1_x][c1_y] != 'x':
            print(n[0] + 1)
            sys.exit(0)
        if board[c1_x][c1_y] == '#' and board[c2_x][c2_y] != '#':
            q.append([[coin1_x, coin1_y], [c2_x, c2_y], [n[0]+1]])
        elif board[c2_x][c2_y] == '#' and board[c1_x][c1_y] != '#':
            q.append([[c1_x, c1_y], [coin2_x, coin2_y], [n[0]+1]])
        elif board[c1_x][c1_y] != '#' and board[c2_x][c2_y] != '#':
            q.append([[c1_x, c1_y], [c2_x, c2_y], [n[0]+1]])
print(-1)