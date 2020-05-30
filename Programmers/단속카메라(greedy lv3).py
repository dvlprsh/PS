//Solve
# 풀이 1 -정확도 100% 효율성 100%
def solution(routes):
    answer = 1
    c_boundary = [0, 0]
    # 1. 진입점 오름차순, 진출점 내림차순
    routes.sort(key =lambda x: (x[0], -x[1]))
    c_boundary[0], c_boundary[1] = routes.pop(0)
    for route in routes:
        l, r = route
        if l > c_boundary[1]:
            answer += 1
            c_boundary[0], c_boundary[1] = l, r
        else:
            c_boundary[0]= max(l, c_boundary[0])
            c_boundary[1]= min(r, c_boundary[1])
        
    return answer

# 풀이 2 -정확도 100% 효율성 20%
'''
1. 구간 길이별 정렬 (짧은 구간 순서로 탐색)
2. 최소 구간을 담은 group 배열
3. 현재 구간이 group 안에 포함되어 있는지, 겹치는 구간이 가장 긴 요소가 무엇인지 완전탐색
    => 시간 초과
'''
def solution(routes):
    answer = 0
    group = []
    # 1. 길이별 정렬
    routes.sort(key =lambda x: x[1]-x[0])
    group.append(routes.pop(0))
    # 2. 교집합 없으면 answer +=1
    for route in routes:
        has_cross = False
        right_point = 0
        left_point = 0
        cross_length = -1
        group_idx = -1
        for i, v in enumerate(group):
            left_in = v[0] >= route[0] and v[0] <= route[1]
            right_in = v[1] >= route[0] and v[1] <= route[1]
            
            if not left_in and not right_in:
                continue
            else:
                has_cross = True
                
            #교집합 최대한 큰 구간 찾기
            if left_in:
                l = max(v[0], route[0])
            else:
                l = v[0]
            if right_in:
                r = min(v[1], route[1])
            else:
                r = v[1]
                
            if r - l > cross_length:
                cross_length = r -l
                group_idx = i
                right_point = r
                left_point = l
              
                
        #교차하는 지점 하나도 없을때
        if not has_cross:
            group.append(route)
        else:
            group[group_idx] = [left_point, right_point]
            
        
        #print(group)
    return len(group)


# 풀이 3 -실패 정확성 100 효율성 0
def solution(routes):
    answer = 0
    routes.sort(key= lambda x: x[1]-x[0], reverse = True)
    
    group = []
    initial = routes.pop()
    set1=set([i for i in range(initial[0], initial[1]+1)])
    group = []
    group.append(set1)

    while routes:
        route = routes.pop()
        current = set([i for i in range(route[0], route[1]+1)])
        idx = -1
        has_cross = False
        max_cross_set = set()
        max_length = -1
        for i, v in enumerate(group):
            cross = current.intersection(v)
         
            if len(cross) == 0:
                continue
            else:
                has_cross = True
                
            if max_length < len(cross):
                max_length = len(cross)
                max_cross_set = cross
                idx = i
            
        if has_cross:
            group[idx] = max_cross_set
        else:
            group.append(current)
     
        
        
    return len(group)
