#풀이 1 - 실패 (정확성 60)
from collections import defaultdict
def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results:
        lose[result[1]].add(result[0])
        win[result[0]].add(result[1])


    for i in range(1, n+1):
        for loser in win[i]:
            win[i] = win[i].union(list(win[loser]))

        for winner in lose[i]:
            lose[i] = lose[i].union(list(lose[winner]))

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            answer+=1

    return answer

#풀이 2 - 성공
from collections import defaultdict
def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results:
        lose[result[1]].add(result[0])
        win[result[0]].add(result[1])

    for i in range(1, n+1):

        for loser in win[i]:
            lose[loser] = lose[loser].union(list(lose[i]))

        for winner in lose[i]:
            win[winner] = win[winner].union(list(win[i]))

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            answer+=1

    return answer
