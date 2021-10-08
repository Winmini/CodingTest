def solution(brown, yellow):
    row = 0
    col = 0
    for i in range(3, 5000):
        row = i
        col = i
        for j in range(i,5000):
            row = j
            if 2*row + 2*col - 4 == brown:
                if row*col - brown == yellow:
                    return [row, col]
            if 2*row + 2*col - 4 > brown:
                break