import sys
import heapq


a = int(input())
M_heap = []
m_heap = []

for i in range(a):
    data = int(sys.stdin.readline())
    if i % 2:
        heapq.heappush(m_heap, data)
    else:
        heapq.heappush(M_heap, -data)
    if m_heap and -M_heap[0] > m_heap[0]:
        heapq.heappush(M_heap, -heapq.heappop(m_heap))
        heapq.heappush(m_heap, -heapq.heappop(M_heap))
    print(-M_heap[0])