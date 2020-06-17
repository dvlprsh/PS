# Solve
# 풀이 1 - 100점
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    s1 = heapq.heappop(scoville)
    if s1 >= K:
        return 0
    while len(scoville) > 0:
        answer += 1
        s2 = heapq.heappop(scoville)
        new_scov = s1 + (s2 * 2)
        heapq.heappush(scoville, new_scov)
        s1 = heapq.heappop(scoville)
        if s1 >= K:
            return answer
    return -1

#풀이 2 - 76.2점 (정확성 100 효율성 0)
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    if min(scoville) >= K:
        return 0
    while len(scoville) > 1:
        answer += 1
        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)
        new_scov = s1 + (s2 * 2)
        heapq.heappush(scoville, new_scov)
        if min(scoville) >= K:
            return answer
    return -1