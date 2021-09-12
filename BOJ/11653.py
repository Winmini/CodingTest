a = int(input())
while a != 1:
    for i in range(2,a+1):
        if not a % i:
            print(i)
            a /= i
            a = int(a)
            break