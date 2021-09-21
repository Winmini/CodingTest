from collections import deque
import sys


a = [int(i) for i in sys.stdin.readline().split()]

deq = deque([i for i in range(1, a[0] + 1)])
answer = []

while deq:
    for i in range(a[1] - 1):
        deq.append(deq[0])
        deq.popleft()
    answer.append(deq[0])
    deq.popleft()
print('<', end='')
for i in answer[:-1]:
    print(i, end=', ')
print(answer[-1], end='')
print('>', end='')