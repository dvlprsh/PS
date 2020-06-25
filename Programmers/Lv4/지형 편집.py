# Solve
# 풀이 1 - 100점
import heapq
def solution(land, P, Q):
    heights = []
    heights_count = {}
    square = len(land) ** 2
    costs = []
    # 2차원 배열 land를 1차 배열로 분해
    for v in land:
        heights.extend(v)
    heights.sort(reverse=True)
    # total_block : 전체 블록 개수
    total_block = sum(heights) 
    # heights_count: 높이별 개수 (key: 높이, value: 해당 높이를 갖는 칸의 개수)
    for v in heights:
        if v not in heights_count:
            heights_count[v] = 1
        else:
            heights_count[v] += 1
    prev_key = -1
    to_delete = 0
    memo = 0 # memo: 높이 k인 줄에서 제거해야 할 블록 개수
    for k, v in heights_count.items():
        if prev_key != -1:
            to_delete += memo * (prev_key - k)
        volume = square * k # volume: 높이 k인 육면체로 만들 경우의 부피
        to_add = volume - (total_block - to_delete)
        heapq.heappush(costs, to_add * P + to_delete * Q)
        prev_key = k
        memo += v

    return heapq.heappop(costs)

#풀이 2 - 시간 초과 64.7점 (높이 0~k 까지 하나씩 순회 => 시간초과)
import heapq
def solution(land, P, Q):
    square = len(land) * len(land[0])
    blocks =[element for array in land for element in array]
    max_height = max(blocks)
    floors = [0 for _ in range(max_height+1)]
    costs = [[] for _ in range(max_height+1)]
    costs_by_height = []
    for i, v in enumerate(blocks):
        if v != 0:
            floors[v] += 1
  
    for i, v in enumerate(reversed(floors)):
        if i < max_height-1:
            floors[max_height-i-1] += v
    
    for i, v in enumerate(floors):
        costs[i] = [(square - v) *P, v*Q]
    costs[0] = [0, 0]
    
    # 최대 높이로 맞출 경우
    total_cost=0
    for v in costs:
        total_cost += v[0]
 
    heapq.heappush(costs_by_height, total_cost)
    
    for i in range(max_height):
        h = max_height-i
        total_cost = total_cost - costs[h][0] + costs[h][1]
        heapq.heappush(costs_by_height, total_cost)
    return heapq.heappop(costs_by_height)