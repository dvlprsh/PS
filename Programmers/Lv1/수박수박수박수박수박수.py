def solution(n):
    answer = ''
    flag = False
    for i in range(n):
        if flag:
            answer += '박'
        else:
            answer += '수'
        flag = not flag
    return answer