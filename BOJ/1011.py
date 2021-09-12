import sys


test_case = int(input())

for T in range(test_case):
    a = [int(i) for i in sys.stdin.readline().split()]
    length = a[1] - a[0]
    k = 1
    while pow(k,2) < length:
        k += 1
    if int((pow(k,2) + pow(k-1,2)) / 2) >= length:
        print(2*k - 2)
    else:
        print(2*k - 1)