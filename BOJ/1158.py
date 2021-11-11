import sys


N, K = [int(i) for i in sys.stdin.readline().split()]
people = [i for i in range(1, N+1)]
loc = 0
answer = []
while people:
    loc += K - 1
    if loc >= len(people):
        loc %= len(people)
    answer.append(people.pop(loc))
print('<', end='')
for i in answer[:-1]:
    print(i, end=', ')
print(answer[-1], end='>')