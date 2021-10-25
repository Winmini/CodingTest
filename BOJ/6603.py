import sys
from itertools import combinations

first = 0
while True:
    t = [int(i) for i in sys.stdin.readline().split()]
    if len(t) == 1:
        sys.exit(0)
    else:
        if first:
            print()
        first = 1
    for i in list(combinations(t[1:], 6)):
        print(' '.join(map(str, i)))