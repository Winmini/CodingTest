import heapq
import sys


N = int(input())
study = []
for _ in range(N):
    study.append([int(i) for i in sys.stdin.readline().split()])
study.sort()
q = []
answer = 0
for i in study:
    if q:
        if q[0] <= i[0]:
            heapq.heappop(q)
            heapq.heappush(q, i[1])
        else:
            heapq.heappush(q, i[1])
            answer += 1
    else:
        heapq.heappush(q, i[1])
        answer += 1
print(answer)