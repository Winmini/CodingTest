def solution(weights, head2head):
    info = [[0]*5 for _ in range(len(weights))]
    for idx, game in enumerate(head2head):
        tmp = game.count('W') + game.count('L')
        if tmp:
            info[idx][0] = (game.count('W')/tmp)
        else:
            info[idx][0] = 0
            
        for j, i in enumerate(game):
            if i == 'W' and weights[idx] < weights[j]:
                info[idx][1] += 1
        info[idx][2] = weights[idx]
        info[idx][3] = len(weights) - idx
        info[idx][4] = idx + 1
    info.sort(reverse=True)
    return [i[-1] for i in info]