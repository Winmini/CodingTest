test_case = int(input())

for T in range(test_case):
    height = int(input())
    num = int(input())
    x = [i for i in range(1, num + 1)]
    y = [sum(x[:i]) for i in range(1, len(x)+1)]
    for i in range(height):
        y = [sum(x[:i]) for i in range(1, len(x) + 1)]
        x = y
    print(x[num-1])
