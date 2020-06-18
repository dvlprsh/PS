# Solve
'''
공급 가능 수량 기준으로 최대 힙 구현
'''
import heapq
def solution(stock, dates, supplies, k):
    answer = 0
    heap = [] # (0: 우선순위 1: 공급 2: 날짜)
    for v in zip(dates, supplies):
        heap.append((-v[1], v[1], v[0]))
    heapq.heapify(heap)
    
    while stock < k:
        save = []
        answer +=1
        while heap:
            s = heapq.heappop(heap)
            if s[2] > stock:
                save.append(s)
                continue
            else:
                stock += s[1]
                break
        for v in save:
            heapq.heappush(heap, v)
    return answer