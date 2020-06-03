#Solve - 깊이우선탐색
def solution(n, computers):
    answer = 0
    _childrens=[[] for _ in range(n)]
    _visited=[False for _ in range(n)]

    for i1, v1 in enumerate(computers):
        for i2, v2 in enumerate(v1):
            if i2 != i1 and v2 == 1:
                _childrens[i1].append(i2)
                
    for i in range(n):
        open_list = []
        if not _visited[i]:
            answer += 1
            open_list.append(i)
        else:
            continue
        while open_list:
            current = open_list.pop()
            _visited[current] = True
            for c in _childrens[current]:
                if not _visited[c]:
                    open_list.append(c)
    return answer