a = int(input())
i = 0
while a % 5:
    a -= 3
    i += 1
    if not a:
        break
    if a < 0:
        i = -1
if i != -1:
    i += (a/5)
    print(int(i))
else:
    print(i)