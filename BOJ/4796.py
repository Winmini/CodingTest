import sys

Case = 1
while True:
    L, P, V = [int(i) for i in sys.stdin.readline().split()]
    if L == P == V == 0:
        break
    print('Case {}: {}'.format(Case, (V//P) * L + min(V % P, L)))
    Case += 1