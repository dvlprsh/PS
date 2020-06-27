#Solve
#풀이1 - 100점
def solution(N, road, K):
    answer = 0
    children = [[] for _ in range(N+1)]
    distance = [0 for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    open_list = [1]
    for v in road:
        children[v[0]].append((v[1], v[2]))
        children[v[1]].append((v[0], v[2]))
    while open_list:
        current = open_list[0]
        min_distance = distance[current]
        # 가장 가까운 노드 찾기
        for i in open_list:
            if distance[i] < min_distance:
                current = i
                min_distance = distance[i]
        open_list.remove(current)
        visited[current] = True
        
        if min_distance <= K:
            answer += 1
        for neighbor in children[current]:
            if neighbor[0] in open_list:
                new_distance = distance[current] + neighbor[1]
                if distance[neighbor[0]] > new_distance:
                    distance[neighbor[0]] = new_distance
            elif not visited[neighbor[0]] and neighbor[0] not in open_list:
                distance[neighbor[0]] = distance[current] + neighbor[1]
                open_list.append(neighbor[0])
    return answer
# 풀이 2 - 84.4 점 (min_distance 찾는 부분 잘못됨)
def solution(N, road, K):
    answer = 0
    children = [[] for _ in range(N+1)]
    distance = [0 for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    open_list = [1]
    for v in road:
        children[v[0]].append((v[1], v[2]))
        children[v[1]].append((v[0], v[2]))
    while open_list:
        min_distance = 2001
        current = 0
        # 가장 가까운 노드 찾기
        for i in open_list:
            if distance[i] < min_distance:
                current = i
                min_distance = distance[i]
        open_list.remove(current)
        visited[current] = True
        
        if min_distance <= K:
            answer += 1
        for neighbor in children[current]:
            if neighbor[0] in open_list:
                new_distance = distance[current] + neighbor[1]
                if distance[neighbor[0]] > new_distance:
                    distance[neighbor[0]] = new_distance
            elif not visited[neighbor[0]] and neighbor[0] not in open_list:
                distance[neighbor[0]] = distance[current] + neighbor[1]
                open_list.append(neighbor[0])
    return answer