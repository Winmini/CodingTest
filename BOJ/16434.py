import sys


N, F_ATK = [int(i) for i in sys.stdin.readline().split()]
room = []
for _ in range(N):
    room.append([int(i) for i in sys.stdin.readline().split()])
MinHP = 1
MaxHP = int(1e14)
answer = 0
while MinHP <= MaxHP:
    ATK = F_ATK
    mean = (MinHP + MaxHP) // 2
    nowHP = mean
    for t, a, h in room:
        if t == 1:
            if h % ATK:
                nowHP -= (h//ATK) * a
            else:
                nowHP -= (h//ATK - 1) * a
            if nowHP <= 0:
                break
        elif t == 2:
            ATK += a
            nowHP += h
            if nowHP > mean:
                nowHP = mean
    if nowHP > 0:
        MaxHP = mean - 1
    else:
        MinHP = mean + 1
print(MinHP)