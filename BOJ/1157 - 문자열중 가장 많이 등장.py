from collections import Counter

a = input().upper()
b = Counter(a).most_common(2)
if len(b) >= 2:
    if b[0][1] == b[1][1]:
        print('?')
    else:
        print(b[0][0])
else:
    print(b[0][0])