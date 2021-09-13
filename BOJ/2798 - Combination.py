import sys
from itertools import combinations


a = [int(i) for i in sys.stdin.readline().split()]
b = sorted([int(i) for i in sys.stdin.readline().split()])
b_com = list(combinations(b, 3))
result = sorted([sum(i) for i in b_com] + [a[1]], reverse=True)
# 혹시 같은 숫자가 있다면 앞에서 부터 검색했을 때 문제가 생기므로 역순으로 정렬
print(result[result.index(a[1])+1])
# 그숫자의 앞인덱스보다 뒤인덱스로 찾으면 된다.