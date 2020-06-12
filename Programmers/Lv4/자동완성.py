# Solve
def get_sim(word1, word2):
    zip_list = list(zip(word1, word2))
    for i, v in enumerate(zip_list):
        if v[0] != v[1]:
            return i
    return len(zip_list)
def solution(words):
    answer = 0
    words.sort()
    for i, v in enumerate(words):
        if i ==0:
            max_sim = get_sim(words[i], words[i+1])
        elif i == len(words) -1:
            max_sim = get_sim(words[i-1], words[i])
        else:
            max_sim = max(get_sim(words[i], words[i+1]), get_sim(words[i-1], words[i]))
        
        if max_sim + 1 > len(v):
            answer += len(v)
        else:
            answer+= max_sim + 1
    return answer
'''
def get_sim(word1, word2):
    두 단어를 한 글자씩 비교해 앞에서부터 동일한 글자 수 반환
def solution(words):
    answer = 0
    words 정렬
    for i, v in enumerate(words):
        max_sim = 다른 단어와 겹치는 최대 글자 수
        (i-1)번째 요소, (i+1)번째 요소와 비교해 가장 큰 유사도 찾기

    if max_sim + 1 > len(v):
            answer += len(v)
        else:
            answer+= max_sim + 1
    return answer
'''