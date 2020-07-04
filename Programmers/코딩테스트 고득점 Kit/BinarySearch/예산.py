#0704 Solve
def solution(budgets, M):
    left = 0
    right = max(budgets)
    while left <= right:
        mid = (left + right) // 2
        total_budget = 0
        for v in budgets:
            if v > mid:
                total_budget += mid
            else:
                total_budget += v
        if total_budget > M:
            right = mid - 1
        else:
            left = mid + 1
    return right