import sys
from itertools import combinations


N = int(input())
S = [int(i) for i in sys.stdin.readline().split()]
answer = S[:]
for i in range(2, N+1):
    for j in list(combinations(S, i)):
        answer.append(sum(j))
answer = sorted(list(set(answer)))
a = 1
for i in answer:
    if i != a:
        break
    a += 1
print(a)