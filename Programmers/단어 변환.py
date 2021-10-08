from collections import deque


def solution(begin, target, words):
    visit = [False] * len(words)
    answer = 0
    now = 0
    
    q = deque([[begin, 0]])
    while q:
        now, answer = q.popleft()
        if now == target:
            break
        for i, w in enumerate(words):
            if visit[i]:
                continue
            cnt = 0
            for b, t in zip(now, w):
                if b == t:
                    cnt += 1
            if cnt != len(begin) - 1:
                continue
            q.append([w, answer + 1])
            visit[i] = True
    if now == target:
        return answer
    else:
        return 0