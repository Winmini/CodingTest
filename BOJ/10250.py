import sys
import math

t_case = int(input())

for T in range(t_case):
    a = [int(i) for i in sys.stdin.readline().split()]
    num = str(math.ceil(a[2] / a[0]))
    if a[2] % a[0]:
        height = str(a[2] % a[0])
    else:
        height = str(a[0])
    if len(num) == 1:
        num = '0' + num
    print(height + num)