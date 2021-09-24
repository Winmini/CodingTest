import sys


size = int(sys.stdin.readline())
house = []
visit = [[0 for _ in range(size)] for _ in range(size)]

for _ in range(size):
    house.append(list(input()))

dir_x = [-1, 0, 1, 0]
dir_y = [0, -1, 0, 1]
q = []
com = []

for idx, row in enumerate(house):
    for idy, col in enumerate(row):
        if col == '1' and visit[idx][idy] == 0:
            tmp = 1
            q.append([idx, idy])
            visit[idx][idy] = 1
            while q:
                now = q.pop(0)
                for n in range(4):
                    pos_x = now[0] + dir_x[n]
                    pos_y = now[1] + dir_y[n]
                    if pos_x < 0 or pos_y < 0 or pos_x >= size or pos_y >= size:
                        continue
                    if visit[pos_x][pos_y] or house[pos_x][pos_y] != '1':
                        continue
                    tmp += 1
                    visit[pos_x][pos_y] = 1
                    q.append([pos_x, pos_y])
            com.append(tmp)
print(len(com))
for i in sorted(com):
    print(i)