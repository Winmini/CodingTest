# https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    music_chart = {}
    answer = []
    for n in range(len(plays)):
        if genres[n] in music_chart:
            music_chart[genres[n]].append([n, plays[n]])
            music_chart[genres[n]][0] += plays[n]
        else:
            music_chart[genres[n]] = [plays[n], [n, plays[n]]]
    music_chart = sorted(music_chart.items(), key = lambda x: x[1][0], reverse = True)
    for m in music_chart:
        answer.append(sorted(m[1][1:], key=lambda x: x[1], reverse = True)[0][0])
        try:
            answer.append(sorted(m[1][1:], key=lambda x: x[1], reverse = True)[1][0])
        except:
            continue
    return answer