import sys

a = [int(i) for i in sys.stdin.readline().split()]

b = []
for i in range(a[0]):
    b.append(input())
c = []

for x in range(a[0] - 7):
    tmp = b[x:x+8]
    for y in range(a[1] - 7):
        bd = [i[y:y+8] for i in tmp]

        first_cnt = 0

        for i in range(8):
            for j in range(8):
                if (i + j) % 2:
                    if bd[i][j] != 'W':
                        first_cnt += 1
                else:
                    if bd[i][j] != 'B':
                        first_cnt += 1

        second_cnt = 0

        for i in range(8):
            for j in range(8):
                if (i + j) % 2:
                    if bd[i][j] != 'B':
                        second_cnt += 1
                else:
                    if bd[i][j] != 'W':
                        second_cnt += 1

        c.append(first_cnt)
        c.append(second_cnt)
print(min(c))