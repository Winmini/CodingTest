import sys


a = int(input())
people = []
for i in range(a):
    people.append([int(i) for i in sys.stdin.readline().split()])

for idx, kw in enumerate(people):
    rank = 1
    for j in people[:idx] + people[idx+1:]:
        if j[0] > kw[0] and j[1] > kw[1]:
            rank+=1
    print(rank, end=' ')