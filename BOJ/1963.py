from collections import deque
import sys


a = [1000, 9999]
pr_set = [True] * (a[1] + 1)
m = int(a[1] ** 0.5)
for i in range(2, m+1):
    if pr_set[i]:
        for j in range(2*i,a[1]+1,i):
            pr_set[j] = False
pr_set[:1000] = [False] * 1000

test_case = int(input())
for _ in range(test_case):
    visit = [False] * 10000
    x, y = [i for i in sys.stdin.readline().split()]
    q = deque([[x, 0]])
    answer = -1
    while q:
        now, num = q.popleft()
        if now == y:
            answer = num
            break
        if visit[int(now)]:
            continue
        visit[int(now)] = True
        for i in range(10):
            if pr_set[int(str(i) + now[1:])]:
                if not visit[int(str(i) + now[1:])]:
                    q.append([str(i)+now[1:], num + 1])
            if pr_set[int(now[0] + str(i) + now[2:])]:
                if not visit[int(now[0] + str(i) + now[2:])]:
                    q.append([now[0] + str(i) + now[2:], num + 1])
            if pr_set[int(now[:2] + str(i) + now[3])]:
                if not visit[int(now[:2] + str(i) + now[3])]:
                    q.append([now[:2] + str(i) + now[3], num + 1])
            if pr_set[int(now[:3] + str(i))]:
                if not visit[int(now[:3] + str(i))]:
                    q.append([now[:3] + str(i), num + 1])
    if answer == -1:
        print('Impossible')
    else:
        print(answer)