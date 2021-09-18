a = int(input())
N = [0] * 1000001
N[1] = 1
N[2] = 2

if a >= 3:
    for i in range(3, a + 1):
        N[i] = (N[i-1] + N[i-2]) % 15746
    print(N[a])
else:
    print(a)