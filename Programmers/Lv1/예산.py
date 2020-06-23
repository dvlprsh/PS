# Solve
def solution(d, budget):
    answer = 0
    d.sort()
    total = 0
    for v in d:
        if total + v <= budget:
            total += v
            answer += 1
        else:
            break
    return answer