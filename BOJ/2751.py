import sys
import heapq


a = int(input())
x = []
for i in range(a):
    heapq.heappush(x, int(sys.stdin.readline()))
for i in range(len(x)):
    print(heapq.heappop(x))