import sys


a = int(input())
b = sorted([int(i) for i in sys.stdin.readline().split()])
answer = 0
for idx, i in enumerate(b):
    answer += (i * (len(b) - idx))
print(answer)