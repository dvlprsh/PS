# Solve
#풀이1 (풀이2 효율성 개선) 100점 (heap 정렬기준 - 작업 소요시간)
import heapq
from collections import deque
def set_duplicate(last):
    # last 보다 요청시점 빠른 작업들 duplicate에 할당 -> 소요시간 오름차순으로 처리
    while _jobs:
        if _jobs[0][0] < last:
            s, d = _jobs.popleft()
            heapq.heappush(_duplicate, (d, s))
        else:
            break
    return
def solution(jobs):
    answer = 0
    global _jobs, _duplicate
    _jobs = deque(sorted(jobs, key = lambda x: (x[0], x[1])))
    _duplicate = [] # (0: 소요시간, 1: 요청시점)
    while _jobs:
        start, duration = _jobs.popleft()
        last = start + duration
        answer += duration
        set_duplicate(last)
        
        while _duplicate:
            d, s = heapq.heappop(_duplicate)
            answer += last - s + d
            last = last + d
            set_duplicate(last)
    return answer // len(jobs)
    
#풀이 2 - 100점 (heap 정렬기준 - 작업 소요시간)
import heapq
def solution(jobs):
    answer = 0
    d_jobs = []
    jobs.sort(key = lambda x: (x[0], x[1]))
    num = len(jobs)
    last = 0
    while jobs:
        start, duration = jobs.pop(0)
        answer +=  duration
        end = start + duration
        last  = end
        while jobs:
            if jobs[0][0] < end:
                d_jobs.append(jobs.pop(0))
            else:
                break
      
        while d_jobs:
            heap = [(v[1], v) for v in d_jobs]
            heapq.heapify(heap)
            shortest = heapq.heappop(heap)
            answer += last - shortest[1][0] + shortest[1][1]
            last = shortest[1][0] + last - shortest[1][0] + shortest[1][1]
            d_jobs.remove(shortest[1])
            while jobs:
                if jobs[0][0] < last:
                    d_jobs.append(jobs.pop(0))
                else:
                    break
    return answer // num


#풀이 3 - 35점 (heap 정렬기준 - 대기시간 + 작업소요시간)
import heapq
def solution(jobs):
    answer = 0
    d_jobs = []
    jobs.sort(key = lambda x: (x[0], x[1]))
    num = len(jobs)
    last = 0
    while jobs:
        heap = []
        start, duration = jobs.pop(0)
        answer +=  duration
        end = start + duration
        last  = end
        while jobs:
            if jobs[0][0] < end:
                d_jobs.append(jobs.pop(0))
            else:
                break
      
        while d_jobs:
            heap = [(last - v[0] + v[1], v) for v in d_jobs]
            heapq.heapify(heap)
            shortest = heapq.heappop(heap)
            answer += shortest[0]
            last = shortest[1][0] + shortest[0]
            d_jobs.remove(shortest[1])
            while jobs:
                if jobs[0][0] < last:
                    d_jobs.append(jobs.pop(0))
                else:
                    break
    return answer // num