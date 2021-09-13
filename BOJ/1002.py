import sys


a = int(input())

for T in range(a):
    data = [int(i) for i in sys.stdin.readline().split()]
    bt_length = (pow(data[0] - data[3], 2) + pow(data[1] - data[4], 2)) ** 0.5
    r1 = data[2]
    r2 = data[5]
    if bt_length == 0 and r1 == r2:
        print(-1) # 동일위치 같은반지름
    elif bt_length == 0 and r1 != r2:
        print(0) # 동일위치 다른반지름
    elif r1 + r2 < bt_length:
        print(0) # 거리 안닿음
    elif r1 + r2 == bt_length or r1 == r2 + bt_length or r2 == r1 + bt_length:
        print(1) # 외접
    elif r1 > r2 + bt_length or r2 > r1 + bt_length:
        print(0) # 한쪽원이 너무큼
    else:
        print(2) # 그외에는 2점이겠지