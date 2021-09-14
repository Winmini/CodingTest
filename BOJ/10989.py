import sys
from collections import Counter


a = int(input())
x = Counter()
for i in range(a):
    x[int(sys.stdin.readline())] += 1
print(list(x.keys()))
for i in sorted(list(x.keys())):
    for j in range(x[i]):
        print(i)