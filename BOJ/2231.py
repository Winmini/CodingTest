a = int(input())
for i in range(a):
    tmp = i
    for j in range(len(str(i))):
        tmp += int(str(i)[j])
    if tmp == a:
        print(i)
        break
    if i == a-1:
        print(0)