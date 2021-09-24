from collections import Counter

import sys


a = [int(i) for i in sys.stdin.readline().split()]
tree = Counter([int(i) for i in sys.stdin.readline().split()])

start = 0
end = max(tree)
while start <= end:
    mid = (start+end)//2
    num = 0
    for i in tree:
        if (i - mid) > 0:
            num += (i - mid) * tree[i]
    if num < a[1]:  # a[1] 은 필요한 나무
        end = mid - 1
    else:
        start = mid + 1
print(end)