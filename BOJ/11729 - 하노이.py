def hanoi(n, start, end, via):
    if n == 1:
        print(start, end)
    else:
        hanoi(n-1, start, via, end)
        print(start, end)
        hanoi(n-1, via, end, start)


a = int(input())
print(pow(2,a)-1)
hanoi(a, 1, 3, 2)