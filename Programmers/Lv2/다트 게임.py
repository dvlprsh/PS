# Solve
from collections import deque
def solution(dartResult):
    total_score = 0
    score = ''
    queue = deque()
    for c in dartResult:
        if len(queue) > 2:
            total_score += queue.popleft()

        if c.isdigit():
            score += c
        else:
            if c == 'S':
                queue.append(int(score) ** 1)
            elif c == 'D':
                queue.append(int(score) ** 2)
            elif c == 'T':
                queue.append(int(score) ** 3)
            elif c == '*':
                queue[-1] *= 2
                if len(queue) > 1:
                    queue[-2] *= 2
            elif c == '#':
                queue[-1] *= -1
            score = ''
    for v in queue:
        total_score += v
    return total_score

'''
total_score = 전체 점수
score = 각 게임당 점수
queue = [] (각 게임당 얻은 점수를 큐에 저장)
for c in dartResult:
    if len(queue) > 2:
        total_score += 가장 마지막에 저장된 점수 pop()

    if c가 숫자인 경우:
        score += c
    else:
        if c == 'S':
            queue.append(int(score) ** 1)
        elif c == 'D':
            queue.append(int(score) ** 2)
        elif c == 'T':
            queue.append(int(score) ** 3)
        elif c == '*':
            queue[-1] *= 2
            if len(queue) > 1:
                queue[-2] *= 2
        elif c == '#':
            queue[-1] *= -1
        score = ''
# 게임 다 끝나면 queue 에 남은 점수 총점에 합산
for v in queue:
    total_score += v
return total_score
'''