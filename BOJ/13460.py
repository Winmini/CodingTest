from collections import deque
import sys


dir_x = [0, 1, 0, -1]
dir_y = [1, 0, -1, 0]

N, M = [int(i) for i in sys.stdin.readline().split()]
board = []
for _ in range(N):
    board.append(list(input()))
red, blue = deque([]), deque([])

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red.append([i, j, -1, 0])
            board[i][j] = '.'
        if board[i][j] == 'B':
            blue.append([i, j])
            board[i][j] = '.'

while red:
    red_x, red_y, d, c = red.popleft()
    blue_x, blue_y = blue.popleft()
    board[red_x][red_y] = 'R'
    board[blue_x][blue_y] = 'B'
    for i in range(4):
        if (d == 2 and i == 0) or (d == 3 and i == 1) or (d == 0 and i == 2) or (d == 1 and i == 3):
            continue
        nr_x = red_x + dir_x[i]
        nr_y = red_y + dir_y[i]
        nb_x = blue_x + dir_x[i]
        nb_y = blue_y + dir_y[i]
        while board[nr_x][nr_y] == '.':
            nr_x += dir_x[i]
            nr_y += dir_y[i]
        while board[nb_x][nb_y] == '.':
            nb_x += dir_x[i]
            nb_y += dir_y[i]
        if board[nb_x][nb_y] == 'O':
            continue
        if board[nr_x][nr_y] == 'O' and board[nb_x][nb_y] == 'R':
            continue
        if board[nr_x][nr_y] == 'O':
            print(c + 1)
            sys.exit(0)
        if board[nr_x][nr_y] == 'B':
            nr_x = nb_x - dir_x[i]
            nr_y = nb_y - dir_y[i]
        if board[nb_x][nb_y] == 'R':
            nb_x = nr_x - dir_x[i]
            nb_y = nr_y - dir_y[i]
        if nr_x != red_x + dir_x[i] or nr_y != red_y + dir_y[i] or nb_x != blue_x + dir_x[i] or nb_y != blue_y + dir_y[i]:
            red.append([nr_x - dir_x[i], nr_y - dir_y[i], i, c+1])
            blue.append([nb_x - dir_x[i], nb_y - dir_y[i]])
        if c > 10:
            print(-1)
            sys.exit(0)
    board[red_x][red_y] = '.'
    board[blue_x][blue_y] = '.'
    if not blue:
        blue.append([blue_x, blue_y])
print(-1)

