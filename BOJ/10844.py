n = [[0 for i in range(10)] for j in range(101)]
a = int(input())
n[1][:] = [1] * 10
n[2][0] = 1
n[2][1:9] = [2] * 8
n[2][9] = 1

for i in range(3, a+1):
    n[i][0] = n[i-1][1]
    for k in range(1, 9):
        n[i][k] = n[i-1][k-1] + n[i-1][k+1]
    n[i][9] = n[i-1][8]

print(sum(n[a][1:]) % 1000000000)