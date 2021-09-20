import sys


a = int(input())

for i in range(a):
    sentence = [i for i in sys.stdin.readline().split()]
    for j in sentence:
        print(j[::-1], end=' ')