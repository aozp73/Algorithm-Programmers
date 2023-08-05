def solution(m, musicinfos):
    # 간편하게 play_time만큼 끊기 위해 1자리로 변환
    def convert(melody):
        melody = melody.replace('C#', 'c')
        melody = melody.replace('D#', 'd')
        melody = melody.replace('F#', 'f')
        melody = melody.replace('G#', 'g')
        melody = melody.replace('A#', 'a')
        return melody

    # 기억하는 멜로디 변환
    m = convert(m)
    answer = ('', '', 0) # title, melody, play_time

    for music in musicinfos:
        start, end, title, melody = music.split(',')
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))

        # 해당 곡 연주 시간을 분단위로 변환
        play_time = 60*(end_h - start_h) + (end_m - start_m)
        # 각 곡 정보 변환
        melody = convert(melody)
        # max : 악보가 A 하나이고, 연주시간 만큼 모든 데이터가 필요할 때
        # average : 악보길이보다 연주시간이 짧을 경우 그만큼 짤라서 진행
        played_melody = (melody * play_time)[:play_time]

        # 기억하는 멜로디가 해당 악보에 들어가 있고, 매번 최대 길이시간의 곡으로 갱신
        if m in played_melody and play_time > answer[2]:
            answer = (title, played_melody, play_time)

    if answer[2] == 0:
        return "(None)"
    else:
        return answer[0]
    
print(solution("ABCDEFG", 	["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
