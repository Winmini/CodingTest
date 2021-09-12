a = int(input())
result = 0
for i in range(a):
    b = input()
    tmp = []
    a = ''
    for j in b:
        if a != j:
            tmp.append(j)
        a = j
    if len(tmp) == len(set(tmp)):
        result +=1
print(result)