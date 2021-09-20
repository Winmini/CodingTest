import sys


a = [int(i) for i in sys.stdin.readline().split()]
coin = []
for i in range(a[0]):
    tmp = int(sys.stdin.readline())
    if tmp < a[1]:
        coin.append(tmp)
answer = 0

while a[1] != 0:
    if a[1] >= coin[-1]:
        answer += (a[1] // coin[-1])
        a[1] -= (a[1] // coin[-1]) * coin[-1]
    else:
        if coin:
            coin.pop()
print(answer)