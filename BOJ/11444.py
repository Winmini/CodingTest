def getFibonacci(n):
    if not fibonacci.get(n):
        if n % 2:
            fibonacci[n] = (getFibonacci((n+1)//2)**2 +
                            getFibonacci((n+1)//2-1)**2) % 1000000007
        else:
            fibonacci[n] = (getFibonacci(n+1) - getFibonacci(n-1)) % 1000000007

    return fibonacci[n]


fibonacci = {0: 0, 1: 1, 2: 1, 3: 2}
print(getFibonacci(int(input())))