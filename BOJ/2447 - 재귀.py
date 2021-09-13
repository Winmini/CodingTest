def sqr(a):
    if a == 1:
        return '*'
    else:
        tmp = sqr(a//3)
        t_b = [i * 3 for i in tmp]
        middle = [i + ' ' * (a//3) + i for i in tmp]
        return t_b + middle + t_b

a = int(input())
for i in sqr(a):
    print(i)