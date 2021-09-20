a = int(input())
money = []
for i in range(a):
    x = int(input())
    if x:
        money.append(x)
    else:
        money.pop()
print(sum(money))