import heapq

a = input()
b = []
for i in a:
    heapq.heappush(b, -int(i))
for i in range(len(b)):
    print(-heapq.heappop(b), end='')