import sys

a = int(input())
num = [int(i) for i in sys.stdin.readline().split()]
answer = [0] * a
stack = [[0, 1000001]]

for idx, i in enumerate(num):
    while stack[-1][1] < i: # 크다면,
        answer[stack[-1][0]] = i
        stack.pop()
    else:
        stack.append([idx, i])
for i in stack[1:]:
    answer[i[0]] = -1
print(*answer)