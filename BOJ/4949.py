import sys


while True:
    stack = []
    sentence = sys.stdin.readline()
    if sentence == '.\n':
        break
    for i in sentence:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    break
            else:
                stack = ['no']
                break
        elif i == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    break
            else:
                stack = ['no']
                break
        if i == '.':
            break
    if stack:
        print('no')
    else:
        print('yes')