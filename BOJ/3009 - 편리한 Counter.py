import sys
from collections import Counter

x = Counter()
y = Counter()
for i in range(3):
    a = [int(i) for i in sys.stdin.readline().split()]
    x[a[0]] += 1
    y[a[1]] += 1
print(x.most_common(2)[-1][0], y.most_common(2)[-1][0])