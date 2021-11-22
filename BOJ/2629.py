import sys


measure_list = set()
n = int(input())
weight = [int(i) for i in sys.stdin.readline().split()]

m = int(input())
chk_list = [int(i) for i in sys.stdin.readline().split()]

measure_list.add(weight[0])
for w in weight[1:]:
    tmp = set(measure_list)
    for m in tmp:
        if m + w not in measure_list:
            measure_list.add(m+w)
        if abs(m-w) not in measure_list:
            measure_list.add(abs(m-w))
        if w not in measure_list:
            measure_list.add(w)

for c in chk_list:
    if c in measure_list:
        print('Y', end=' ')
    else:
        print('N', end=' ')