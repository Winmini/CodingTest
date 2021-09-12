import sys


a = int(input())
b = [int(i) for i in sys.stdin.readline().split()]
pr = 0
for i in b:
    if i==2:
        pr +=1
    elif i > 2:
        for j in range(2, i):
            if not i%j:
                break
            if j == i - 1:
                pr += 1
print(pr)