from collections import deque
import sys

test_case = int(input())


for T in range(test_case):
    tmp_order = sys.stdin.readline()[:-1]
    tmp_order.replace('RR', '')
    order = deque()
    for i in tmp_order:
        order.append(i)
    size = int(input())
    tmp = input()
    li = []
    for i in tmp[1:-1].split(','):
        if str.isdigit(i):
            li.append(i)
    while order:
        if order[0] == 'R':
            li = li[::-1]
            order.popleft()
        elif order[0] == 'D':
            if li:
                li.pop(0)
                order.popleft()
            else:
                li = 'error'
                break
    if li == 'error':
        print('error')
    else:
        answer = '['
        for i in li:
            answer += i
            answer += ','
        answer = answer[:-1] + ']'
        print(answer)