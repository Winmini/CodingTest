import sys


a = [int(i) for i in sys.stdin.readline().split()]
line = []
for i in range(a[0]):
    line.append(int(input()))

start = 1
end = max(line)


while start <= end:
    mid = (start+end)//2
    num = 0
    for i in line:
        num += (i//mid)
    if num < a[1]:
        end = mid - 1
    else:
        start = mid + 1
print(end)