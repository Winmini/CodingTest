import bisect
import sys

n = int(input())
a = [int(i) for i in sys.stdin.readline().split()]

lis = [a[0]]
ans = 1

for num in a[1:]:
    if lis[-1] < num:
        lis.append(num)
        ans += 1
    else:
        lis[bisect.bisect_left(lis, num)] = num
print(ans)