# Solve
'''
dict = 색인 번호 Hash Table
색인 번호 초기화
while msg 길이 > 0:
    while dict에 없는 w 찾을 때까지 반복:
        if dict 에 w 있으면:
            if msg에 남은 글자 있으면:
                다음 한 글자 추가
                continue
            else:
                answer에 (w) 색인번호 등록
                break
        else: 없으면 dict 에 등록하고
            answer에 (w-1) 색인번호 등록
            w-1 만큼 msg 잘라내기
'''
from collections import deque
def solution(msg):
    answer = []
    last_idx = 27
    # 색인 번호 초기화
    dict = {}
    for i in range (26):
        dict[chr(65 + i)] = i+1
    msg = deque(msg)
    while msg:
        w = ''
        while True:
            w += msg.popleft()
            if w in dict:
                if msg:
                    continue
                else:
                    answer.append(dict[w])
                    break
            else:
                dict[w] = last_idx
                last_idx +=1
                msg.appendleft(w[-1])
                answer.append(dict[w[0:-1]])
                break
    return answer