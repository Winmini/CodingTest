def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        l = len(phone_book[i])
        if phone_book[i][0:l]==phone_book[i+1][0:l]:
            return False
    return True

# 효율성 한문제 탈락모델
# def solution(phone_book):
#     phone_book.sort(key=len)
#     for i in range(10):
#         x_data = []
#         y_data = []
#         n_data = []
#         l = len(phone_book[0])
#         for i in phone_book:
#             if len(i) == l:
#                 x_data.append(i)
#             else:
#                 y_data.append(i[:l])
#                 n_data.append(i)
#         for i in x_data:
#             if i in y_data:
#                 return False
#         if not n_data:
#             return True
#         else:
#             phone_book = n_data

# 효율성 2문제 탈락
# def solution(phone_book):
#     phone_book.sort(key=len)
#     x_data = ["x"]
#     for i in phone_book:
#         for j in x_data:
#             if i[:len(j)] == j:
#                 return False
#         x_data.append(i)
#     return True