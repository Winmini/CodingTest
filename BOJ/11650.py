import sys


a = int(input())
b = []
for i in range(a):
    b.append([int(i) for i in sys.stdin.readline().split()])
for i in sorted(b):
    print(i[0], i[1])