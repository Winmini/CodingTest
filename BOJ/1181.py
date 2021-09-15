a = int(input())
b = []
for i in range(a):
    b.append(input())

b = list(set(b))
for i in sorted(b, key=lambda x: (len(x), x)):
    print(i)