# Solve
# 스택 사용 - 100
def solution(s):
    answer = 0
    stack = []
    for c in s:
        if len(stack) == 0:
            stack.append(c)
        elif stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    if len(stack) == 0:
        return 1
    else:
        return 0
# 시간 초과 65.2
def solution(s):
    while True:
        prev_s = s
        for i in range(97, 123):
            c = chr(i)
            if c in s:
                cc = c+c
                s =''.join(s.split(cc))
            else:
                continue
        if s == prev_s:
            return 0
        elif len(s) == 0:
            return 1
# 시간초과 30점
def solution(s):
    while True:
        has_same = False
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                s = s[0:i] + s[i+2:]
                has_same = True
                break
        if not has_same:
            break
            
    if len(s) == 0:
        return 1
    else:
        return 0