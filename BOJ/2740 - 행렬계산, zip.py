import sys


a = [int(i) for i in sys.stdin.readline().split()]
A = []
for j in range(a[0]):
    A.append([int(i) for i in sys.stdin.readline().split()])
b = [int(i) for i in sys.stdin.readline().split()]
B = []
for j in range(b[0]):
    B.append([int(i) for i in sys.stdin.readline().split()])

C = [[sum(i * j for i, j in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

for i in C:
    print(*i)