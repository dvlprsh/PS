# Solve
# 풀이 1 - 100점
import math
def solution(n, stations, w):
    answer = 0
    stations = [(v-w, v+w) for v in stations]
    start = 1
    for i, v in enumerate(stations):
        if start < v[0]:
            end = v[0]-1
            answer += math.ceil((end - start +1) / (w * 2 + 1))
        start = v[1] + 1
        if i == len(stations)-1:
            if start <= n:
                answer += math.ceil((n - start +1) / (w * 2 + 1))
    return answer
    
# 풀이2 - 93.3 점 (마지막 1칸 남았을 경우 예외처리 못함)
import math
def solution(n, stations, w):
    answer = 0
    stations = [(v-w, v+w) for v in stations]
    start = 1
    for i, v in enumerate(stations):
        if start < v[0]:
            end = v[0]-1
            answer += math.ceil((end - start +1) / (w * 2 + 1))
        start = v[1] + 1
        if i == len(stations)-1:
            if start < n:
                answer += math.ceil((n - start +1) / (w * 2 + 1))
    return answer