# ceil 올림, round(n)반올림
import sys
import math


a = [int(i) for i in sys.stdin.readline().split()]
height = a[2] - a[0]
day = height / (a[0] - a[1])
print(int(math.ceil(day)) + 1)