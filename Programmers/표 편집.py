class row:
    def __init__(self, data):
        self.data = data
        self.up = None
        self.down = None


def solution(n, k, cmd):
    excel = [row(i) for i in range(n)]
    top = row(-1)
    bot = row(-1)
    top.down = excel[0]
    excel[0].up = top
    bot.up = excel[-1]
    excel[-1].down = bot
    
    erase_list = []
    for i in range(n-1):
        excel[i].down = excel[i+1]
        excel[i+1].up = excel[i]
        
    k = excel[k]
    for order in cmd:
        order = order.split()
        if order[0] == 'U':
            for _ in range(int(order[-1])):
                k = k.up
        if order[0] == 'D':
            for _ in range(int(order[-1])):
                k = k.down
        if order[0] == 'C':
            erase_list.append(k)
            if k.down == bot:
                bot.up = k.up
                k.up.down = bot
                k = bot.up
            else:
                k.up.down = k.down
                k.down.up = k.up
                k = k.down
        if order[0] == 'Z':
            if erase_list:
                r = erase_list.pop()
                r.up.down = r
                r.down.up = r
    ans = ['X'] * n
    answer = top.down
    
    while answer.down:
        ans[answer.data] = 'O'
        answer = answer.down
    return ''.join(ans)