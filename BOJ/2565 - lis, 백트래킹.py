import sys

a = int(input())
lines = []
for i in range(a):
    lines.append([int(i) for i in sys.stdin.readline().split()])
lines = sorted(lines, key=lambda x: x[0])
answer = [500]
# 모든 전깃줄 초기화 및 정렬
x = [0] * a
x[0] = 1
for i in range(1, a):
    if lines[i][1] > lines[i-1][1]:
        tmp = []
        for idx, j in enumerate(lines[:i]):
            if j[1] < lines[i][1]:
                tmp.append(x[idx] + 1)
        x[i] = max(tmp)
    else:
        tmp = []
        for idx, j in enumerate(lines[:i][::-1]):
            if j[1] < lines[i][1]:
                tmp.append(x[i-idx-1] + 1)
        if not tmp:
            x[i] = 1
        else:
            x[i] = max(tmp)
print(len(lines) - max(x))




# 백트래킹 풀이, 시간초과
# import sys
#
#
# a = int(input())
# lines = []
# for i in range(a):
#     lines.append([int(i) for i in sys.stdin.readline().split()])
# lines = sorted(lines, key=lambda x: x[0])
# answer = [500]
# # 모든 전깃줄 초기화 및 정렬
#
#
# def cut_the_lines(x, line):
#     if x >= min(answer):
#         return
#     cross = [0] * len(line)
#     for idx, k in enumerate(line):
#         for idy, j in enumerate(line[idx+1:]):
#             if k[1] > j[1]:
#                 cross[idx] += 1
#                 cross[idy + idx + 1] += 1
#     if sum(cross) == 0:
#         answer.append(x)
#         return
#     else:
#         for w in range(len(line)):
#             if cross[w]:
#                 n_line = line[:w] + line[w+1:]
#                 cut_the_lines(x+1, n_line)
#
#
# cut_the_lines(0, lines)
# print(answer)
# print(min(answer))