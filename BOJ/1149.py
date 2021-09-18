import sys



X = [0] * 1001
k = int(input())
pr = [[0 for j in range(1001)] for i in range(1001)]

first = [int(i) for i in sys.stdin.readline().split()]
pr[1][0] = first[0]
pr[1][1] = first[1]
pr[1][2] = first[2]
if k == 1:
    print(min(first))
    sys.exit(0)
second = [int(i) for i in sys.stdin.readline().split()]
pr[2][0] = min(pr[1][1], pr[1][2]) + second[0]
pr[2][1] = min(pr[1][0], pr[1][2]) + second[1]
pr[2][2] = min(pr[1][0], pr[1][1]) + second[2]
if k == 2:
    print(min(pr[:3]))
    sys.exit(0)

for i in range(3, k + 1):
    tmp = [int(i) for i in sys.stdin.readline().split()]
    pr[i][0] = min(pr[i - 1][1], pr[i - 1][2]) + tmp[0]
    pr[i][1] = min(pr[i - 1][0], pr[i - 1][2]) + tmp[1]
    pr[i][2] = min(pr[i - 1][0], pr[i - 1][1]) + tmp[2]
    X[i] = min(pr[i][0], pr[i][1], pr[i][2])

print(X[k])