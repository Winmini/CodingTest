import sys


n = int(input())
prime = sorted([int(i) for i in sys.stdin.readline().split()])
if n % 2:
    print(prime[n//2] ** 2)
else:
    print(prime[0] * prime[-1])