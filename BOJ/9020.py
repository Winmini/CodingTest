import sys
a = 10000
b = [True] * (2 * a + 1)
m = int(a ** 0.5)
for i in range(2, m + 1):
    if b[i]:
        for j in range(2 * i, a + 1, i):
            b[j] = False
pr_list = [i for i in range(2, a + 1) if b[i]]


test_case = int(sys.stdin.readline())
for T in range(test_case):
    a = int(sys.stdin.readline())
    for i in range(a//2, 1, -1):
        if i in pr_list and a-i in pr_list:
            print(i, a-i)
            break