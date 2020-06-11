'''
def normalize(melody):
    normalize - '#' 들어간 음 처리하는 함수
    '#' 들어간 음은 소문자로 변환
    ex) AC# => Ac
    return 변환한 멜로디
def solution(m, musicinfos):
    answer = '(None)'
    max_time = 조건 일치하는 음악 중 최대 재생시간
    m = normalize(m)
    
    for v in musicinfos:
        v = v.split(',')
        m1, s1 = (시작 시간) 분, (시작 시간) 초
        m2, s2 = (끝난 시간) 분, (끝난 시간) 초
        play_time = 재생시간
        original_melody = 곡 원본 멜로디
        played_melody = 전체 재생된 멜로디
        if 멜로디 일치 and 최대 재생시간 갱신:
            answer  = v[2]
            max_time = play_time
    return answer
'''
def normalize(melody):
    n_melody = ''
    melody = melody.split('#')
    for i, v in enumerate(melody):
        v = list(v)
        if i != len(melody)-1:
            v[-1] = v[-1].lower()
        n_melody += ''.join(v)
    return n_melody

def solution(m, musicinfos):
    answer = '(None)'
    max_time = 0
    m = normalize(m)
    
    for v in musicinfos:
        v = v.split(',')
        m1, s1 = list(map(int, v[0].split(':')))
        m2, s2 = list(map(int, v[1].split(':')))
        play_time = (60 * m2 + s2) - (60 * m1 + s1)
        original_melody = normalize(v[3])
        played_melody = (original_melody * (play_time // len(original_melody) + 1))[0: play_time]
        if m in played_melody and play_time > max_time:
            answer  = v[2]
            max_time = play_time
    return answer