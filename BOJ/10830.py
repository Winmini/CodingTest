import sys


def matrix_sq(mat):
    return [[sum(x * y for x, y in zip(A_row, A_col)) % 1000 for A_col in zip(*mat)] for A_row in mat]


a = [int(i) for i in sys.stdin.readline().split()]
A = []
for j in range(a[0]):
    A.append([int(i) % 1000 for i in sys.stdin.readline().split()])


tmp = []
for i in range(36, 0, -1):
    if a[1] >= pow(2, i):
        a[1] -= pow(2, i)
        tmp.append(i)


answer = []
for i in tmp:
    tmp_mat = A
    for j in range(i):
        tmp_mat = matrix_sq(tmp_mat)
    answer.append(tmp_mat)

if a[1] == 1:
    answer.append(A)

if len(answer) == 1:
    for i in answer:
        for j in i:
            print(*j)
else:
    result = answer[0]
    for i in answer[1:]:
        result = [[sum(x * y for x, y in zip(A_row, A_col)) % 1000 for A_col in zip(*result)] for A_row in i]

    for i in result:
        print(*i)