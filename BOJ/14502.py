import copy
from itertools import combinations
from collections import deque
import sys


dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]

R, C = [int(i) for i in sys.stdin.readline().split()]
board = []
for _ in range(R):
    board.append([int(i) for i in sys.stdin.readline().split()])
q = deque([])
sp = []
for idx, row in enumerate(board):
    for idy, col in enumerate(row):
        if col == 2:
            q.append([idx, idy])
        elif col == 0:
            sp.append([idx, idy])

answer = 0

for wall in list(combinations(sp, 3)):
    t_board = copy.deepcopy(board)
    t_q = copy.deepcopy(q)
    for idx, idy in wall:
        t_board[idx][idy] = 1
    while t_q:
        now_x, now_y = t_q.popleft()
        for i in range(4):
            cur_x = now_x + dir_x[i]
            cur_y = now_y + dir_y[i]
            if cur_x < 0 or cur_y < 0 or cur_x == R or cur_y == C:
                continue
            if t_board[cur_x][cur_y]:
                continue
            t_board[cur_x][cur_y] = 2
            t_q.append([cur_x, cur_y])
    ans = 0
    for row in t_board:
        ans += row.count(0)
    answer = max(ans, answer)
print(answer)