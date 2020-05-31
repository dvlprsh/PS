#풀이 1, 2 실패 이유 - lost와 reserve 공통된 값 삭제하는 부분이 잘못되었음
#풀이 1 - 실패 (정확성 75)
def solution(n, lost, reserve):
    answer = n

    for i, v in enumerate(reserve):
        if v in lost:
            del reserve[i]
            del lost[lost.index(v)]

    for i, v in enumerate(reserve):
        if v-1 in lost:
            del lost[lost.index(v-1)]
        elif v+1 in lost:
             del lost[lost.index(v+1)]

    answer -= len(lost)
    return answer

#풀이 2 - 실패 (정확성 75)
def solution(n, lost, reserve):
    answer = n
    able_list = []
    for i, v in enumerate(reserve):
        if v in lost:
            del reserve[i]
            del lost[lost.index(v)]

    for i, v in enumerate(reserve):
        if v-1 in lost and v+1 in lost:
            able_list.append({'to': [v-1, v+1], 'able': 2})
        elif v-1 in lost:
            able_list.append({'to': [v-1], 'able': 1})

        elif v+1 in lost:
            able_list.append({'to': [v+1], 'able': 1})

    for k in sorted(able_list, key=(lambda x: x['able'])):
        for to in k['to']:
            if to in lost:
                del lost[lost.index(to)]
                break

    answer -= len(lost)
    return answer


#풀이 3 -성공(솔루션 참고)
def solution(n, lost, reserve):
    answer = n

    _lost = [l for l in lost if l not in reserve]
    _reserve = [r for r in reserve if r not in lost]

    for i, v in enumerate(_reserve):
        if v-1 in _lost:
            del _lost[_lost.index(v-1)]
        elif v+1 in _lost:
            del _lost[_lost.index(v+1)]

    answer -= len(_lost)
    return answer

#풀이 4 -성공
def solution(n, lost, reserve):
    answer = n
    _reserve = reserve[:]
    _lost = lost[:]
    for i, v in enumerate(reserve):
        if v in lost:
            _reserve.remove(v)
            _lost.remove(v)

    for i, v in enumerate(_reserve):
        if v-1 in _lost:
            del _lost[_lost.index(v-1)]
        elif v+1 in _lost:
             del _lost[_lost.index(v+1)]

    answer -= len(_lost)
    return answer