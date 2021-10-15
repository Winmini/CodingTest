import sys


def bk(pre, now, d):
    if pre == 0:
        if now == 1:
            if saw[now][2] != saw[now+1][6]:
                bk(now, 2, -d)
        elif now == 2 or now == 3:
            if saw[now][2] != saw[now+1][6]:
                bk(now, now + 1, -d)
            if saw[now][6] != saw[now-1][2]:
                bk(now, now-1, -d)
        elif now == 4:
            if saw[now][6] != saw[now-1][2]:
                bk(now, now-1, -d)
    else:
        if now != 1 and now != 4:
            if pre > now:
                if saw[now][6] != saw[now - 1][2]:
                    bk(now, now-1, -d)
            else:
                if saw[now][2] != saw[now + 1][6]:
                    bk(now, now+1, -d)
    if d == 1:
        saw[now] = saw[now][-1] + saw[now][:-1]
    else:
        saw[now] = saw[now][1:] + saw[now][0]


saw = ['0']
for _ in range(4):
    saw.append(sys.stdin.readline().split()[0])
num = int(input())
for _ in range(num):
    n, dt = [int(i) for i in sys.stdin.readline().split()]
    bk(0, n, dt)
answer = int(saw[1][0]) + 2*int(saw[2][0]) + 4*int(saw[3][0]) + 8*int(saw[4][0])
print(answer)