import sys



N, M = [int(i) for i in sys.stdin.readline().split()]
start, end = 0, 1
per = [int(i) for i in sys.stdin.readline().split()]
answer = 0
subSum = 0
while end != len(per) + 1 or subSum > M:
    subSum = sum(per[start:end])
    if subSum == M:
        answer += 1
        end += 1
    elif subSum > M:
        start += 1
    else:
        end += 1

print(answer)