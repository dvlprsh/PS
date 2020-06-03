# Solve - 너비우선탐색
# 풀이 1
def solution(begin, target, words):
    if target not in words:
        return 0
    else:
        t_index = words.index(target)

    answer = 0
    words.append(begin)
    _len = len(begin)
    _sets = [i for i in words]
    _children = [[] for _ in range(len(words))]
    _parent = [-1 for _ in range(len(words))]
    open_list = []
    closed_list = []
   
    for i, word in enumerate(words):
        for i2, v2 in enumerate(_sets):
            if i != i2:
                count =0
                for _i in range(_len):
                    if word[_i] != v2[_i]:
                        count +=1
                    if count >= 2:
                        break
                if count == 1:
                    _children[i].append(i2)
                
    words.pop()
    open_list.append(len(words))
    
    while open_list:
        current = open_list.pop(0)
        closed_list.append(current)
        if current == t_index:

            while current != len(words):
                answer+=1
                current = _parent[current]
            return answer

        for node in _children[current]:
            if node in closed_list or node in open_list:
                continue
            _parent[node] = current
            open_list.append(node)

    return answer
# 풀이 2-정확성 80 (테스트케이스 3 실패)
# 같은 문자 중복해서 들어간 단어의 경우 생각못함 ex) ssssfs, fsssss
def solution(begin, target, words):
    if target not in words:
        return 0
    else:
        t_index = words.index(target)

    answer = 0
    words.append(begin)
    _len = len(begin)
    _sets = [set(i) for i in words]
    _children = [[] for _ in range(len(words))]
    _parent = [-1 for _ in range(len(words))]
    open_list = []
    closed_list = []
    
    for i, word in enumerate(words):
        w_set = set(word)

        for i2, v2 in enumerate(_sets):
            if i != i2:
                if len(w_set & v2) == _len-1:
                    _children[i].append(i2)
    words.pop()
    open_list.append(len(words))
    
    while open_list:
        current = open_list.pop(0)
        closed_list.append(current)
        if current == t_index:

            while current != len(words):
                answer+=1
                current = _parent[current]
            return answer

        for node in _children[current]:
            if node in closed_list or node in open_list:
                continue
            _parent[node] = current
            open_list.append(node)

    return answer