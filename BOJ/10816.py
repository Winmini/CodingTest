from collections import Counter
import sys


x = int(input())
a = Counter([int(i) for i in sys.stdin.readline().split()])
y = int(input())
for i in [int(i) for i in sys.stdin.readline().split()]:
    print(a[i], end=' ')
