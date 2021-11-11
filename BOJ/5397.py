t = int(input())
for i in range(t):
    s1 = []
    s2 = []
    li = input()
    for txt in li:
        if txt == '<':
            if s1:
                s2.append(s1.pop())
        elif txt == '>':
            if s2:
                s1.append(s2.pop())
        elif txt == '-':
            if s1:
                s1.pop()
        else:
            s1.append(txt)
    s1.extend(reversed(s2))
    print(''.join(s1))