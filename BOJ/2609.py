import sys


def gcd(a, b):
    if b:
        return gcd(b, a % b)
    else:
        return a


N = sorted([int(i) for i in sys.stdin.readline().split()])
answer = gcd(N[0], N[1])
print(answer)
print(N[0] * N[1] // answer)