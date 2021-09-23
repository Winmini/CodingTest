import sys


a = [int(i) for i in sys.stdin.readline().split()]

print(pow(a[0] % a[2], a[1], a[2]))