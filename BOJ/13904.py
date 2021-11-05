import heapq
import sys

N = int(input())
assignment = []
for _ in range(N):
    assignment.append([int(i) for i in sys.stdin.readline().split()])
assignment.sort(reverse=True)
answer = []
i = 1
while i != N + 1 and assignment:
    while assignment:
        if len(answer) < i:
            heapq.heappush(answer, assignment.pop()[1])
        elif assignment[-1][0] <= i:
            if answer[0] < assignment[-1][1]:
                heapq.heappop(answer)
                heapq.heappush(answer, assignment.pop()[1])
            else:
                assignment.pop()
        else:
            break
    i += 1
print(sum(answer))
