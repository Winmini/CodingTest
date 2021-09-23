import math
from collections import deque
import sys


a = [int(i) for i in sys.stdin.readline().split()]
x = deque([i for i in range(1, a[0] + 1)]) # 숫자리스트
queue = [int(i) for i in sys.stdin.readline().split()] # 찾아야 하는 숫자
size = len(x)
answer = 0
while True:
    if x[0] == queue[0]:
        x.popleft()
        queue.pop(0)
        if not queue:
            break
    else:
        if x.index(queue[0]) < math.ceil(len(x)/2):
            x.append(x[0])
            x.popleft()
            answer += 1
        else:
            x.appendleft(x[-1])
            x.pop()
            answer += 1
print(answer)