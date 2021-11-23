import sys


dir_x = [0, 0, 1, -1]  # 동서남북
dir_y = [1, -1, 0, 0]


def robot(x, y, k, state, cnt): # 0이 단순
    global complicated
    global simple
    if state:
        complicated += cnt
        return
    if k == n:
        simple += cnt
        return
    else:
        for i in range(4):
            cur_x = x + dir_x[i]
            cur_y = y + dir_y[i]
            if visit[cur_x][cur_y] or state:
                visit[cur_x][cur_y] += 1
                robot(cur_x, cur_y, k+1, 1, cnt * weight[i])
            else:
                visit[cur_x][cur_y] += 1
                robot(cur_x, cur_y, k+1, 0, cnt * weight[i])
            visit[cur_x][cur_y] -= 1


n, E, W, S, N = [int(i) for i in sys.stdin.readline().split()]
weight = [E/100, W/100, S/100, N/100]
simple = 0
complicated = 0
visit = [[0] * 100 for _ in range(100)]
visit[50][50] = 1
robot(50, 50, 0, 0, 1)
print(simple / (simple + complicated))