from collections import deque


a = int(input())

deq = deque([i for i in range(1, a + 1)])
while len(deq) != 1:
    deq.popleft()
    deq.append(deq[0])
    deq.popleft()
print(deq[0])