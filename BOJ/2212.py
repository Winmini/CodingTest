import sys

N = int(input())
K = int(input())
sensor = sorted([int(i) for i in sys.stdin.readline().split()])
diff = []
for i in range(N-1):
    diff.append(sensor[i + 1] - sensor[i])
diff.sort(reverse=True)
answer = 0
if N-K > 0:
    for i in range(N-K):
        answer += diff.pop()
    print(answer)
else:
    print(answer)