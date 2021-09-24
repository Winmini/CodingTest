import sys

case = int(input())

for _ in range(case):
    size = [int(i) for i in sys.stdin.readline().split()]
    bug = [[0 for _ in range(size[0])] for _ in range(size[1])]
    visit = [[0 for _ in range(size[0])] for _ in range(size[1])]

    for _ in range(size[2]):
        bug_loc = [int(i) for i in sys.stdin.readline().split()]
        bug[bug_loc[1]][bug_loc[0]] = 1

    dir_x = [-1, 0, 1, 0]
    dir_y = [0, -1, 0, 1]
    q = []
    com = []

    for idx, row in enumerate(bug):
        for idy, col in enumerate(row):
            if col == 1 and visit[idx][idy] == 0:
                tmp = 1
                q.append([idx, idy])
                visit[idx][idy] = 1
                while q:
                    now = q.pop(0)
                    for n in range(4):
                        pos_x = now[0] + dir_x[n]
                        pos_y = now[1] + dir_y[n]
                        if pos_x < 0 or pos_y < 0 or pos_x >= size[1] or pos_y >= size[0]:
                            continue
                        if visit[pos_x][pos_y] or bug[pos_x][pos_y] != 1:
                            continue
                        tmp += 1
                        visit[pos_x][pos_y] = 1
                        q.append([pos_x, pos_y])
                com.append(tmp)
    print(len(com))