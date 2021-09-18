N = [0] * 101
N[1] = 1
N[2] = 1
N[3] = 1
N[4] = 2
N[5] = 2
for i in range(6, 101):
    N[i] = (N[i-1] + N[i-5])

a = int(input())
for t in range(a):
    k = int(input())
    print(N[k])