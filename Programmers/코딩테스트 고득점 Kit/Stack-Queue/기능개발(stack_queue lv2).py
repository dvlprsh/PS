from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        task = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        for i in range(len(progresses)):
            if progresses[0] >= 100:
                task += 1
                progresses.popleft()
                speeds.popleft()
        if task > 0:
            answer.append(task)
            task = 0

    return answer