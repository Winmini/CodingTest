from collections import deque
import sys


a = int(input())

heap = deque([])

for i in range(a):
    order = a = [i for i in sys.stdin.readline().split()]
    if order[0] == 'push':
        heap.append(order[-1])
    elif order[0] == 'front':
        if heap:
            print(heap[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if heap:
            print(heap[-1])
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(heap))
    elif order[0] == 'pop':
        if heap:
            print(heap[0])
            heap.popleft()
        else:
            print(-1)
    elif order[0] == 'empty':
        if heap:
            print(0)
        else:
            print(1)