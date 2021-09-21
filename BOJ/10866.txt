from collections import deque
import sys

deq = deque([])

a = int(input())

for i in range(a):
    order = [i for i in sys.stdin.readline().split()]
    if order[0] == 'push_back':
        deq.append(order[1])
    elif order[0] == 'push_front':
        deq.appendleft(order[1])
    elif order[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)
    elif order[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(deq))
    elif order[0] == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif order[0] == 'pop_back':
        if deq:
            print(deq[-1])
            deq.pop()
        else:
            print(-1)
    elif order[0] == 'pop_front':
        if deq:
            print(deq[0])
            deq.popleft()
        else:
            print(-1)