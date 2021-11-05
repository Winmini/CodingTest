import sys


N, K = [int(i) for i in sys.stdin.readline().split()]
order = [int(i) for i in sys.stdin.readline().split()]
now = set()
for i in order:
    now.add(i)
    if len(now) == N:
        break
answer = 0

for i in range(N, len(order)):
    tmp = set()
    if order[i] in now:
        continue
    else:
        for j in order[i:]:
            if j in now:
                tmp.add(j)
            if len(tmp) == N-1:
                t = now - tmp
                now.remove(t.pop())
                now.add(order[i])
                break
        if 0 < len(tmp) < N-1:
            t = now - tmp
            now.remove(t.pop())
            now.add(order[i])
        elif len(tmp) == 0:
            now.pop()
            now.add(order[i])
        answer += 1

print(answer)
