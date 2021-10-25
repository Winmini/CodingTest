N = int(input())
words = []
for _ in range(N):
    words.append(list(input().strip()))
alphabet_match = [0] * 26
for i in words:
    size = len(i)
    for j in range(size):
        alphabet_match[ord(i[j]) - 65] += pow(10, (size - j - 1))
alphabet_match.sort(reverse=True)
answer, cnt = 0, 9
for i in alphabet_match:
    answer += cnt * i
    cnt -= 1
print(answer)