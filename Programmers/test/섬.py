'''
일단 다 연결 => children
[섬1, 섬2, 비용]
비용 기준 정렬

'''
def solution(n, costs):
    answer = 0
    _children = [[] for _ in range(n)]
    v_chilren = []
    visited = []
    costs.sort(key = lambda x: x[2])

    #자식 설정
    for i, v in enumerate(costs):
        node1, node2, cost = v
        _children[node1].append([node2, cost])
        _children[node2].append([node1, cost])
    first = costs.pop(0)
    visited.append(first[0])
    visited.append(first[1])
    answer += first[2]
    v_chilren.extend(_children[first[0]])
    v_chilren.extend(_children[first[1]])

    while True:
        if len(visited) == n:
            break
        v_chilren.sort(key = lambda x: x[1])
        for i, v in enumerate(v_chilren):
           
            node = v[0]
            if not node in visited:
                visited.append(node)
                v_chilren.extend(_children[node])
                answer += v[1]
                break
            
         
 
    return answer