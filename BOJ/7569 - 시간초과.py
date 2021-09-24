import itertools
import sys


size = [int(i) for i in sys.stdin.readline().split()]
# 가로, 세로, 높이
tomato = []
visit = [[[0 for _ in range(size[0])] for _ in range(size[1])] for _ in range(size[2])]

for h in range(size[2]):
    tmp = []
    for _ in range(size[1]):
        tmp.append([int(i) for i in sys.stdin.readline().split()])
    tomato.append(tmp)

dir_x = [-1, 0, 1, 0, 0, 0]
dir_y = [0, -1, 0, 1, 0, 0]
dir_h = [0, 0, 0, 0, 1, -1]
q = []
com = []
tomato_loc = []
for idh, h in enumerate(tomato):
    for idx, row in enumerate(h):
        for idy, col in enumerate(row):
            if col == 1:
                q.append([idx, idy, idh])
                visit[idh][idx][idy] = 1
day = -1
while True:
    tq = []
    while q:
        now = q.pop(0)
        for n in range(6):
            pos_x = now[0] + dir_x[n]
            pos_y = now[1] + dir_y[n]
            pos_z = now[2] + dir_h[n]
            if pos_x < 0 or pos_y < 0 or pos_x >= size[1] or pos_y >= size[0] or pos_z < 0 or pos_z >= size[2]:
                continue
            if tomato[pos_z][pos_x][pos_y] or visit[pos_z][pos_x][pos_y]:
                continue
            visit[pos_z][pos_x][pos_y] = 1
            tomato[pos_z][pos_x][pos_y] = 1
            tq.append([pos_x, pos_y, pos_z])
    day += 1
    if not tq:
        break
    q = tq

if 0 in list(itertools.chain(*list(itertools.chain(*tomato)))):
    print(-1)
else:
    print(day)