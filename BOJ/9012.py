import sys


a = int(input())

for i in range(a):
    sentence = sys.stdin.readline()
    if sentence[0] == ')':
        print('NO')
        continue
    stack = []
    for j in sentence:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                stack = ['no']
                break
    if stack:
        print('NO')
    else:
        print('YES')