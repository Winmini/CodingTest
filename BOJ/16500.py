import sys

a = 0
S = sys.stdin.readline().split()[0]
N = int(input())
A = []
for _ in range(N):
    tmp = sys.stdin.readline().split()[0]
    if tmp in S:
        A.append(tmp)
    if tmp == S:
        print(1)
        sys.exit(0)
answer = []
for word in A:
    if S[:1] == word[:1]:
        answer.append(word)
size = len(S)
while answer:
    tmp = []
    for i, ans in enumerate(answer):
        for word in A:
            if S[len(ans):len(ans)+len(word)] == word:
                if len(answer[i] + word) <= size:
                    tmp.append(answer[i] + word)
    answer = []
    for i in tmp:
        if i == S:
            a = 1
            break
        if i in S and i not in answer:
            answer.append(i)
print(a)