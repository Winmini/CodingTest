a = int(input())
x = []
for i in range(666, 3000000):
    if '666' in str(i):
        x.append(i)
x.sort()
print(x[a-1])