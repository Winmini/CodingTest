import sys


def gcd(a, b):
    if b:
        return gcd(b, a % b)
    else:
        return a


testCase = int(input())
for _ in range(testCase):
    N = sorted([int(i) for i in sys.stdin.readline().split()])
    print(N[0] * N[1] // gcd(N[0], N[1]))