import sys


a = int(input())
km = [int(i) for i in sys.stdin.readline().split()]
oil = [int(i) for i in sys.stdin.readline().split()]
now_price = oil[0]
oil.pop()  # 맨마지막 가격은 필요 없음
oil.pop(0) # 맨처음   가격도 필요 없음
answer = now_price * km[0]
km.pop(0)

for idx, i in enumerate(oil):
    if now_price <= i:
        answer += (now_price * km[idx])
    else:
        now_price = i
        answer += (now_price * km[idx])
print(answer)