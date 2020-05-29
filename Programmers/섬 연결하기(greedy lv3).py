//Solve
#풀이 1
def set_candidate(island):
    for v in island :
        if v[0] not in _visited:
            _candidates.append(v)

def solution(n, costs):
    global _candidates, _visited
    answer = 0
    _islands = {}
    _candidates = []
    costs.sort(key= lambda x: x[2])
    _visited = []
    
    for cost in costs:
        node1 = cost[0]
        node2 = cost[1]
        expense = cost[2]
        if node1 not in _islands:
            _islands[node1]=[]
        _islands[node1].append((node2, expense))
        
        if node2 not in _islands:
            _islands[node2]=[]
        _islands[node2].append((node1, expense))   
     
    n1, n2, c=costs[0]
    _visited.append(n1)
    _visited.append(n2)
    set_candidate(_islands[n1])
    set_candidate(_islands[n2])
    answer += c
  
    while _candidates:
        if len(_visited) == n:
            return answer
        
        _candidates.sort(key= lambda x: x[1])
        next = _candidates.pop(0)
        
        if next[0] in _visited:
            continue
        else:
            _visited.append(next[0])
            set_candidate(_islands[next[0]])
            answer+=next[1]
            continue
                
    return answer

# 풀이 2 - 풀이 1 보다 수행시간 약간 더 빠름 (0.05ms 이내)
def set_candidate(island):
    for v in island :
        if v[0] not in _visited:
            _candidates.append(v)

def solution(n, costs):
    global _candidates, _visited
    answer = 0
    _islands = {}
    _candidates = []
    costs.sort(key= lambda x: x[2])
    _visited = []
    
    for cost in costs:
        node1 = cost[0]
        node2 = cost[1]
        expense = cost[2]
        if node1 not in _islands:
            _islands[node1]=[]
        _islands[node1].append((node2, expense))
        
        if node2 not in _islands:
            _islands[node2]=[]
        _islands[node2].append((node1, expense))   
     
    n1, n2, c=costs[0]
    _visited.append(n1)
    _visited.append(n2)
    set_candidate(_islands[n1])
    set_candidate(_islands[n2])
    answer += c
  
    while len(_visited) != n:
        _candidates.sort(key= lambda x: x[1])
        while _candidates:
            next = _candidates.pop(0)
            if next[0] in _visited:
                continue
            else:
                _visited.append(next[0])
                set_candidate(_islands[next[0]])
                answer+=next[1]
                break
                
    return answer

