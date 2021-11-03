from itertools import combinations


shorts = []
for _ in range(9):
    shorts.append(int(input()))

for i in list(combinations(shorts, 7)):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break