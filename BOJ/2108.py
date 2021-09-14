import sys
from collections import Counter


a = int(input())
x = Counter()
for i in range(a):
    x[int(sys.stdin.readline())] += 1
y = sorted(list(x.elements()))
print(round(sum(y)/len(y)))
print(y[(len(y)-1)//2])
z = []
for i in list(x.keys()):
    if x[i] == x.most_common(1)[0][1]:
        z.append(i)
z.sort()
if len(z) >= 2:
    print(z[1])
else:
    print(z[0])
print(max(y)-min(y))