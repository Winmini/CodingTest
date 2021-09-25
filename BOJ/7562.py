import sys


test_case = int(input())
for _ in range(test_case):
    size = int(sys.stdin.readline())
    visit = [[0 for _ in range(size)] for _ in range(size)]

    dir_x = [-1, -1, 1, 1, -2, 2, -2, 2]
    dir_y = [-2, 2, -2, 2, -1, -1, 1, 1]

    loc = [int(i) for i in sys.stdin.readline().split()]
    des = [int(i) for i in sys.stdin.readline().split()]

    q = [[loc[0], loc[1]]]
    ans = 0
    chk = 0
    if loc == des:
        print(0)
    else:
        while True:
            tq = []
            while q:
                now = q.pop(0)
                for n in range(8):
                    pos_x = now[0] + dir_x[n]
                    pos_y = now[1] + dir_y[n]
                    if pos_x < 0 or pos_y < 0 or pos_x >= size or pos_y >= size:
                        continue
                    if visit[pos_x][pos_y]:
                        continue
                    if pos_x == des[0] and pos_y == des[1]:
                        chk = 1
                    visit[pos_x][pos_y] = 1
                    tq.append([pos_x, pos_y])
            ans += 1
            q = tq
            if chk:
                break
        print(ans)