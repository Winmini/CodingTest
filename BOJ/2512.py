import sys


N = int(input())
budget = [int(i) for i in sys.stdin.readline().split()]
M = int(input())
start, end = 0, max(budget)
while start <= end:
    mid = (start + end) // 2
    num = 0
    for money in budget:
        if money >= mid:
            num += mid
        else:
            num += money
    if num <= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)