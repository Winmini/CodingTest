import sys

w = [[[0 for i in range(21)] for j in range(21)] for k in range(21)]
w[0][0][0] = 1
w[1][1][1] = 2
w[2][2][2] = 4

a = [1, 1, 1]

for i in range(0, 21):
    for j in range(0, 21):
        for k in range(0, 21):
            if i <= 0 or j <= 0 or k <= 0:
                w[i][j][k] = 1
            elif i < j < k:
                w[i][j][k] = w[i][j][k-1] + w[i][j-1][k-1] - w[i][j-1][k]
            else:
                w[i][j][k] = w[i-1][j][k] + w[i-1][j-1][k] + w[i-1][j][k-1] - w[i-1][j-1][k-1]


while True:
    a = [int(i) for i in sys.stdin.readline().split()]
    if a[0] == -1 and a[1] == -1 and a[2] == -1:
        break
    if a[0] <= 0 or a[1] <= 0 or a[2] <= 0:
        print('w({}, {}, {}) = {}'.format(a[0], a[1], a[2], w[0][0][0]))
    elif a[0] > 20 or a[1] > 20 or a[2] > 20:
        print('w({}, {}, {}) = {}'.format(a[0], a[1], a[2], w[20][20][20]))
    else:
        print('w({}, {}, {}) = {}'.format(a[0], a[1], a[2], w[a[0]][a[1]][a[2]]))