import sys

n = int(input())
a = [0] + [int(i) for i in sys.stdin.readline().split()]

lis = [[0] * 2 for _ in range(n + 1)]
lis[1] = [1, 1] # 1개, 1번에서옴.
for num in range(2, n + 1):
    tmp = []
    for idx, i in enumerate(a[:num]):
        if i < a[num]:
            tmp.append([lis[idx][0], idx])
    tmp.sort(key=lambda x: x[0], reverse=True)
    lis[num][0] = tmp[0][0] + 1
    lis[num][1] = tmp[0][1]
start_index = 0
for i in zip(*lis):
    start_index = i.index(max(i))
    break

answer = [a[start_index]]
tmp = lis[start_index][1]
for i in range(lis[start_index][0] - 1):
    answer.append(a[tmp])
    tmp = lis[tmp][1]
print(len(answer))
print(*answer[::-1])