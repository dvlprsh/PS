# Solve 
# 풀이 1 - 정확성 100 효율성 100
'''
동적계획법 + 이진탐색
idea - 배열 길이 2 ~ len(cookie)일 경우 나올 수 있는 경우의 수 memo 에 저장

def solution(cookie):
    answer = -1
    max_half = 0 (한 아들이 받을 수 있는 최대 과자 수)
    memo = [[cookie[i]] for i in range(len(cookie)-1)]

    for i in range(1, len(cookie)):
        memo = cookie를 (i + 1) 길이로 잘라서 만들 수 있는 경우의 수 
        for v in memo:
            memo 구하기
            c_sum = 두 아들에게 줄 수 있는 과자 수 총 합
            c_sum_half = c_sum/2

            if max_half > c_sum_half or c_sum % 2 != 0:
                continue
            else:
                이진탐색으로 현재 배열(v)에서 c_sum_half가 존재하는지

                if c_sum_half가 존재하면:
                    if c_sum_half > max_half:
                        max_half = c_sum_half            
        memo.pop()
'''
def solution(cookie):
    answer = -1
    max_half = 0
    memo = [[cookie[i]] for i in range(len(cookie)-1)]
  
    for i in range(1, len(cookie)):
        for v in memo:
            v.append(v[-1]+cookie[i])
            i +=1
            c_sum = v[-1]
            c_sum_half = c_sum/2
            if max_half > c_sum_half or c_sum % 2 != 0:
                continue
            else:
                left = 0
                right = len(v)-1
                has_half = False
                while left <= right:
                    mid = (left+ right) // 2
                    if v[mid] == c_sum_half:
                        has_half = True
                        break
                    if c_sum_half > v[mid]:
                        left = mid + 1
                    else:
                        right = mid - 1
                if has_half:
                    if c_sum_half > max_half:
                        max_half = c_sum_half
                    
        memo.pop()
    return max_half

# 풀이 2  정확성 100 효율성 5/8
def solution(cookie):
    answer = -1
    max_half = 0
    c_len = len(cookie)
    memo = [[cookie[i]] for i in range(c_len-1)]
  
    for i in range(1, c_len):
        for v in memo:
            v.append(v[-1]+cookie[i])
            i +=1
        _memo = sorted(memo, key=lambda x: x[-1], reverse = True)
        for v in _memo:
            c_sum = v[-1]
            c_sum_half = c_sum/2
            if max_half > c_sum_half:
                break
            if c_sum % 2 != 0:
                continue
            else:
                if c_sum_half in v:
                    if c_sum_half > max_half:
                        max_half = c_sum_half
                    break
        memo.pop()
    return max_half

# 풀이 3 - 97.4점
def solution(cookie):
    answer = 0
    c_len = len(cookie)+1
    
    for i in range(c_len-2):
        c_len -= 1
        max_sum = 0
        for j in range(i+1):
            c_cookie = cookie[j:j + c_len]
            c_sum = sum(c_cookie)
            if c_sum % 2 != 0:
                continue
            else:
                half_sum = 0
                for _i, _v in enumerate(c_cookie):
                    half_sum += _v
                   
                    if half_sum == c_sum/2:
                        if half_sum > max_sum:
                            max_sum= half_sum
                        break
                    elif half_sum > c_sum/2:
                        break
        if max_sum != 0:
            return max_sum
        
    return answer