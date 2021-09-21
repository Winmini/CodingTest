from collections import deque
import sys

deq = deque

test_case = int(input())

for T in range(test_case):
    num = [int(i) for i in sys.stdin.readline().split()]
    prime = [int(i) for i in sys.stdin.readline().split()]
    deq = deque([[idx, i] for idx, i in enumerate(prime)])
    x = deque(sorted(prime, reverse=True))
    cnt = 0
    while True:
        if deq[0][1] != x[0]:
            deq.append(deq[0])
            deq.popleft()
        else:
            tmp = deq[0][0]
            deq.popleft()
            x.popleft()
            cnt += 1
            if tmp == num[1]:
                break
    print(cnt)