# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    answer = ['0']
    for i in s:
        if answer[-1] == i:
            del answer[-1]
        else:
            answer.append(i)
    if len(answer) == 1:
        return 1
    else:
        return 0

# 테스트케이스 13이 안됨
# def solution(s):
#     s = list(s)
#     CHK = 1
#     while CHK:
#         tmp = ''
#         result = []
#         CHK = 0
#         for i in s:
#             if tmp == i:
#                 del result[-1]
#                 tmp = ''
#                 CHK = 1
#             else:
#                 if result:
#                     if i == result[-1]:
#                         del result[-1]
#                         tmp = ''
#                         CHK = 1
#                 else:
#                     result.append(i)
#                     tmp = i
#         s = result
#     if s:
#         return 0
#     else:
#         return 1
    