import sys


N, L = [int(i) for i in sys.stdin.readline().split()]
tape = [0] * 1001
for i in sys.stdin.readline().split():
    tape[int(i)] = 1

answer = 0
i = 1
while i <= 1000:
    if tape[i]:
        answer += 1
        i += L - 1
    i += 1
print(answer)