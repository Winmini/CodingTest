from collections import deque


import sys


testCase = int(input())
for _ in range(testCase):
    order = input()
    n = int(input())
    if n:
        arr = deque(sys.stdin.readline().replace("[", "").replace("]", "").replace("\n", "").split(","))
    else:
        trash = input()
        arr = deque([])
    tmp = 0
    for i in range(len(order)):
        if order[i] == "R":
            if tmp == 0:
                tmp = -1
            else:
                tmp = 0
        if order[i] == "D":
            if arr:
                if tmp == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                tmp = 1
                break
    arr = list(arr)
    if tmp == -1 and arr:
        arr = arr[::-1]
    if tmp == 1:
        print("error")
    elif tmp != 1 and arr:
        print("[", end="")
        for i in arr[:-1]:
            print(i, end=",")
        print(arr[-1], end="]")
        print()
    else:
        print([])