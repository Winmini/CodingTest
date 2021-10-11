import sys

n = int(input())
a = [int(i) for i in sys.stdin.readline().split()]
answer = [a[0]]
for i in range(len(a) - 1):
    answer.append(max(answer[i] + a[i + 1], a[i + 1]))
print(max(answer))