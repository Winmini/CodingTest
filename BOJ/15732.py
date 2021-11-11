import sys


N, K, d = [int(i) for i in sys.stdin.readline().split()]
rule = []
for _ in range(K):
    rule.append([int(i) for i in sys.stdin.readline().split()])
answer = 0
high = N
low = 1

t_answer = []
for i, j, k in rule:
    t_answer.append(i + ((j - i)//k)*k)
t_answer = max(t_answer)

while low <= high:
    D = d
    mean = (high + low) // 2
    answer = mean
    for st, ed, n in rule:
        if st <= answer:
            D -= (min(answer, ed) - st) // n + 1
    if D <= 0:
        high = mean - 1
    elif D > 0:
        low = mean + 1

print(min(low, t_answer))