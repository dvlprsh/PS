def solution(s):
    answer = []
    sets = [i.strip('{}').split(',') for i in s[1:len(s)-1].split('},')]
    sets.sort(key= lambda x: len(x))

    for v in sets:
        diff = list(set(v)-set(answer))
        answer.append(diff[0])
    
    return [int(i) for i in answer]