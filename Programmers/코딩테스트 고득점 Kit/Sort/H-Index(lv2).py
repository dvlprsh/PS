# 풀이 참고
def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()
 
    for i, v in enumerate(citations):
        if v >= n-i:
            return n-i
    return answer

# 실패 - 문제를 잘 못 이해함. h-index가 citations 내부 아이템일 필요는 없다.
def solution(citations):
    answer = 0
    citations.sort(reverse = True)
   
    for i, v in enumerate(citations):
        if i+1 >= v and len(citations)-i-1 <= v:
            return v
    return answer