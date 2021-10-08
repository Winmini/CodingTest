from math import ceil


def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    name = dict()
    for i, n in enumerate(enroll):
        name[n] = i
    graph = [[] for _ in range(len(enroll) + 1)]
    for i, n in enumerate(referral):
        if n != '-':
            graph[name[enroll[i]]].append(name[n])
    
    for sel, amt in zip(seller, amount):
        pf = amt * 100
        q = [[name[sel], pf]]
        while q:
            now, money = q.pop()
            if money < 10:
                answer[now] += money
            else:
                answer[now] += ceil(money * 0.9)
                for i in graph[now]:
                    q.append([i, int(money * 0.1)])
    return answer