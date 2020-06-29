# Solve
def solution(s):
    answer = 0
    #최대 팰린드롬 길이가 홀수인 경우
    for idx in range(len(s)):
        for i in range(len(s) // 2 + 1):
            if (idx -i)>=0 and (idx+i) < len(s):
                if s[idx -i] == s[idx +i]:
                    answer = max(answer, i*2 + 1)
                else:
                    break
            else:
                break         
 	  #최대 팰린드롬 길이가 짝수인 경우
    for idx in range(len(s)-1):
        if s[idx] != s[idx + 1]:
            continue
        for i in range(len(s) // 2):
            if idx -i >=0 and idx+1+i <len(s):
                if s[idx -i] == s[idx +1+i]:
                    answer = max(answer, i*2 + 2)
                else:
                    break
            else:
                break
    return answer