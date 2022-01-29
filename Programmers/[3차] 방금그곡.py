def solution(m, musicinfos):
    answer = []
    m = m.replace("C#", "c")
    m = m.replace("D#", "d")
    m = m.replace("F#", "f")
    m = m.replace("G#", "g")
    m = m.replace("A#", "a")
    for idx, musicinfo in enumerate(musicinfos):
        st, et, title, music = musicinfo.split(',')
        music = music.replace("C#", "c")
        music = music.replace("D#", "d")
        music = music.replace("F#", "f")
        music = music.replace("G#", "g")
        music = music.replace("A#", "a")
        l = int(et[:2]) * 60 + int(et[3:]) - int(st[:2]) * 60 - int(st[3:])
        print(((l // len(music) + 1) * music)[:l])
        if m in ((l // len(music) + 1) * music)[:l]:
            answer.append([title, idx, l])
    if answer:
        answer.sort(key = lambda x: (-x[2], x[1]))
        return answer[0][0]
    else:
        return "(None)"