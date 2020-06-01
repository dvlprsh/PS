//Solve
from itertools import permutations
def solution(baseball):
    answer = 0
    cases = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
    
    for case in cases:
        flag = True
        for v in baseball:
            strike = 0
            ball = 0
            b_numbers=list(str(v[0]))
            for i, n in enumerate(b_numbers):
                if case[i] == int(n):
                    strike += 1
                if int(n) in case and int(n) != case[i]:
                    ball += 1
              
            if strike != v[1] or ball != v[2]:
                flag = False
                break
        if flag:
            answer +=1
    return answer