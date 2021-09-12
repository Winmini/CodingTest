import sys

a = [int(i) for i in sys.stdin.readline().split()]
b = [True] * (a[1] + 1)
m = int(a[1] ** 0.5)
for i in range(2, m+1):
    if b[i]:
        for j in range(2*i,a[1]+1,i):
            b[j] = False
if a[0] == 1:
    a[0] = 2
for k in [i for i in range(a[0], a[1]+1) if b[i]]:
    print(k)