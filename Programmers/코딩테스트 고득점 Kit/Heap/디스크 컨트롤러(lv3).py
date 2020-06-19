# Solve
#풀이 1 - 100점 (heap 정렬기준 - 작업 소요시간)
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


#풀이 2 - 35점 (heap 정렬기준 - 대기시간 + 작업소요시간)
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