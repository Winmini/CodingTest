import sys


n, s = (int(i) for i in sys.stdin.readline().split())
seq = [int(i) for i in sys.stdin.readline().split()]
start = -1
end = 1
answer = 100000
seq_sum = []
tmp = 0
for i in seq:
    tmp += i
    seq_sum.append(tmp)
while end != len(seq):
    tmp = 0
    if start == -1:
        tmp = seq_sum[end]
    else:
        tmp = seq_sum[end] - seq_sum[start]
    if tmp >= s:
        if answer > end - start:
            answer = end - start
        start += 1
    else:
        end += 1
if answer == 100000:
    print(0)
else:
    print(answer)