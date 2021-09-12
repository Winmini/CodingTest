# https://programmers.co.kr/learn/courses/30/lessons/17677

def solution(str1, str2):
    # 문자열자르기
    x = []
    y = []
    for i in range(len(str1)-1):
        x.append(str1[i:i+2])
    for i in range(len(str2)-1):
        y.append(str2[i:i+2])   
    
    # 특수문자 없애고 대문자로 넣기.
    xx = []
    yy = []
    for i in range(len(x)):
        if x[i].isalpha():
            xx.append(x[i].upper())
    for i in range(len(y)):
        if y[i].isalpha():
            yy.append(y[i].upper())
            
    if not xx:
        if not yy:
            return 65536 # 공집합이면 계산안한다.
        
    xx_len = len(xx)
    yy_len = len(yy)
    both = 0
    for i in xx:
        if i in yy:
            yy.remove(i)
            both += 1

    if not (xx_len + yy_len - both):
        return 65536
    else:    
        result = (both) / (xx_len + yy_len - both)
        result *= 65536
    return int(result)