def solution(numbers, hand):
    answer = ''
    Lh = '00'
    Rh = '20'
    loc = {'1':'03', '2':'13', '3':'23', '4':'02', '5':'12', '6':'22', '7':'01', '8':'11', '9':'21', '0':'10'}
    for tmp in numbers:
        if tmp == 1 or tmp == 4 or tmp == 7:
            answer += 'L'
            Lh = loc[str(tmp)]
        if tmp == 3 or tmp == 6 or tmp == 9:
            answer += 'R'   
            Rh = loc[str(tmp)]
        if tmp == 2 or tmp == 5 or tmp == 8 or tmp == 0:
            L_line = abs(int(loc[str(tmp)][0]) - int(Lh[0])) + abs(int(loc[str(tmp)][1]) - int(Lh[1]))
            R_line = abs(int(loc[str(tmp)][0]) - int(Rh[0])) + abs(int(loc[str(tmp)][1]) - int(Rh[1]))
              
            if L_line == R_line:
                answer += hand[0].upper()
                if hand[0].upper() == 'L':
                    Lh = loc[str(tmp)]   
                else:
                    Rh = loc[str(tmp)]
            elif L_line < R_line:
                answer += 'L'
                Lh = loc[str(tmp)]
            else:
                answer += 'R'
                Rh = loc[str(tmp)]
    return answer