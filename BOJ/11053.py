import sys


a = int(input())

seq = [0] + [int(i) for i in sys.stdin.readline().split()]

max_seq = [0] * 1001
max_seq[1] = 1
for i in range(2, a + 1):
    if seq[i] > seq[i-1]:
        tmp = [0]
        for idx, j in enumerate(seq[:i]):
            if j < seq[i]:
                tmp.append(max_seq[idx])
        max_seq[i] = max(tmp) + 1
    else:
        tmp = [0]
        for idx, j in enumerate(seq[:i-1][::-1]):
            if j < seq[i]:
                tmp.append(max_seq[i-2-idx])
        max_seq[i] = max(tmp) + 1
print(max(max_seq))