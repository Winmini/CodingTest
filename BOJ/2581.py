tmp1 = int(input())
tmp2 = int(input())
b = [i for i in range(tmp1, tmp2+1)]
c = []
for i in b:
    if i == 2:
        c.append(i)
    elif i > 2:
        for j in range(2, i):
            if not i % j:
                break
            if j == i - 1:
                c.append(i)
if c:
    print(sum(c))
    print(c[0])
else:
    print(-1)