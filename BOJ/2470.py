import sys


size = int(input())
seq = sorted([int(i) for i in sys.stdin.readline().split()])
start = 0
end = len(seq) - 1
answer = int(3e9)
result = []
while start < end:
    if seq[start] + seq[end] == 0:
        result = [seq[start], seq[end]]
        break
    elif seq[start] + seq[end] > 0:
        if abs(seq[start] + seq[end]) < answer:
            result = [seq[start], seq[end]]
            answer = abs(seq[start] + seq[end])
        end -= 1
    else:
        if abs(seq[start] + seq[end]) < answer:
            result = [seq[start], seq[end]]
            answer = abs(seq[start] + seq[end])
        start += 1
print(*result)