import sys


a = int(input())
b = [int(i) for i in sys.stdin.readline().split()]
c = sorted(list(set(b)))
d = {}
for idx, i in enumerate(c):
    d[i] = idx
for i in b:
    print(d[i], end=' ')