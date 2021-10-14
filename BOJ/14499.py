import sys


R, C, x, y, n = [int(i) for i in sys.stdin.readline().split()]
board = []
for _ in range(R):
    board.append([int(i) for i in sys.stdin.readline().split()])
order = [int(i) for i in sys.stdin.readline().split()]
dice = {'top': 0, 'up': 0, 'left': 0, 'right': 0, 'down': 0, 'bot': 0}
for i in order:
    if i == 1:
        if y + 1 == C:
            continue
        y += 1
        dice['left'], dice['top'], dice['right'], dice['bot'] = \
            dice['bot'], dice['left'], dice['top'], dice['right']
    elif i == 2:
        if y == 0:
            continue
        y -= 1
        dice['left'], dice['top'], dice['right'], dice['bot'] = \
            dice['top'], dice['right'], dice['bot'], dice['left']
    elif i == 3:
        if x == 0:
            continue
        x -= 1
        dice['top'], dice['up'], dice['bot'], dice['down'] = \
            dice['down'], dice['top'], dice['up'], dice['bot']
    elif i == 4:
        if x + 1 == R:
            continue
        x += 1
        dice['top'], dice['up'], dice['bot'], dice['down'] = \
            dice['up'], dice['bot'], dice['down'], dice['top']
    if board[x][y] == 0:
        board[x][y] = dice['bot']
    else:
        dice['bot'] = board[x][y]
        board[x][y] = 0
    print(dice['top'])