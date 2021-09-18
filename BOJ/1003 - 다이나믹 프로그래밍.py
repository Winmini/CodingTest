num0 = [0] * (pow(10, 6) + 1)
num1 = [0] * (pow(10, 6) + 1)

# 0의 개수 + 1의 개수


a = int(input())
num0[0] = 1
num1[0] = 0
num0[1] = 0
num1[1] = 1

for t in range(a):
    k = int(input())
    for i in range(2, k + 1):
        num0[i] = num0[i - 1] + num0[i - 2]
        num1[i] = num1[i - 1] + num1[i - 2]
    print(num0[k], num1[k])