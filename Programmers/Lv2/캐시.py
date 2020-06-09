#Solve
'''
    cache = []
    for city in cities:
        if chache 에 city가 존재하면:
            cache에서 city 제거
            cache 맨 뒤에 city 삽입
            answer += 1
        else:
            cache 맨 뒤에 city 삽입
            cache 맨 앞 요소 제거
            answer += 5
'''
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            if len(cache) > cacheSize:
                cache.popleft()
            answer += 5
    return answer