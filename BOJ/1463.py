a = int(input())
d = [0] * (a + 1)

if a <= 1:
    d[1] = 0
    print(d[a])
else:
    for i in range(2, a+1):
        d[i] = d[i-1] + 1
        if not i % 2:
            d[i] = min(d[i//2] + 1, d[i])
        if not i % 3:
            d[i] = min(d[i//3] + 1, d[i])
    print(d[a])