import sys


while True:
    start = [int(i) for i in sys.stdin.readline().split()]
    if start[0] == 0 and start[1] == 0:
        break
    if start[0] % start[1] == 0:
        print('multiple')
    elif start[1] % start[0] == 0:
        print('factor')
    else:
        print('neither')