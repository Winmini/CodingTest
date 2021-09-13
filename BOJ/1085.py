import sys


a = [int(i) for i in sys.stdin.readline().split()]
print(min(a[0], a[1], a[2]-a[0], a[3]-a[1]))