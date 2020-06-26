# Solve
from itertools import combinations
def solution(nums):
    answer = 0
    combi = list(combinations(nums, 3))
    for v in combi:
        _sum = sum(v)
        is_prime = True
        for i in range(2, _sum):
            if _sum % i == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1

    return answer