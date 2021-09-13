import sys


while True:
    a = sorted([int(i) for i in sys.stdin.readline().split()])
    if not a[0]:
        break
    if pow(a[0],2) + pow(a[1],2) == pow(a[2],2):
        print('right')
    else:
        print('wrong')