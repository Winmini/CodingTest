import sys


x = int(input())
a = set([int(i) for i in sys.stdin.readline().split()])
y = int(input())
for i in [int(i) for i in sys.stdin.readline().split()]:
    if i in a:
        print(1)
    else:
        print(0)