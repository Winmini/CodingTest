firstString = input()
secondString = input()

lcs = [[0] * (len(firstString) + 1) for _ in range(len(secondString) + 1)]
for j in range(len(firstString)):
    for i in range(len(secondString)):
        if firstString[j] == secondString[i]:
            lcs[i+1][j+1] = lcs[i][j] + 1
        else:
            lcs[i+1][j+1] = max(lcs[i][j+1], lcs[i+1][j])

print(lcs[-1][-1])
