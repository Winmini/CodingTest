import sys
import heapq

heap_plus = []
heap_minus = []
n = int(input())
for i in range(n):
    order = int(sys.stdin.readline())
    if order > 0:
        heapq.heappush(heap_plus, order)
    elif order < 0:
        heapq.heappush(heap_minus, -order)
    else:
        if heap_plus and heap_minus:
            if heap_plus[0] >= heap_minus[0]:
                print(-heap_minus[0])
                heapq.heappop(heap_minus)
            elif heap_plus[0] < heap_minus[0]:
                print(heap_plus[0])
                heapq.heappop(heap_plus)
        elif heap_plus and not heap_minus:
            print(heap_plus[0])
            heapq.heappop(heap_plus)
        elif heap_minus and not heap_plus:
            print(-heap_minus[0])
            heapq.heappop(heap_minus)
        else:
            print(0)