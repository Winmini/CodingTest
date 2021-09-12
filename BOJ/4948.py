a = int(input())
while a
    b = [True]  (2a + 1)
    m = int((2a)  0.5)
    for i in range(2, m+1)
        if b[i]
            for j in range(2i,2a+1,i)
                b[j] = False
    print(len([i for i in range(a+1, 2a+1) if b[i]]))
    a = int(input())