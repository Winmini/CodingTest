import bisect
import sys


a = [int(i) for i in sys.stdin.readline().split()]
house = []
for i in range(a[0]):
    house.append(int(input()))
house = sorted(house)
min_length = 1
max_length = house[-1] - house[0]
median = 0
while median != max_length:
    median = (min_length + max_length) // 2
    divide = 0
    cnt = 0
    while divide < len(house):
        cnt += 1
        divide = bisect.bisect_left(house, house[divide] + median)
    if cnt < a[1]:
        max_length = median - 1
    elif cnt >= a[1]:
        min_length = median + 1
print(median)