import sys
from math import ceil

test_room = int(input())
t = [int(i) for i in sys.stdin.readline().split()]
B, C = [int(i) for i in sys.stdin.readline().split()]
answer = test_room + sum([ceil((i-B)/C) for i in t if i-B > 0])
print(answer)
