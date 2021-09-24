import sys
import heapq

heap = []
n = int(input())
for i in range(n):
    order = int(sys.stdin.readline())
    if order:
        heapq.heappush(heap, -order)
    else:
        if heap:
            print(-heap[0])
            heapq.heappop(heap)
        else:
            print(0)