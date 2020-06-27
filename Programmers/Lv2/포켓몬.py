# Solve
def solution(nums):
    answer = 0
    nums_count = {}
    for n in nums:
        if n in nums_count:
            nums_count[n] += 1
        else:
            nums_count[n] = 1
    
    if len(nums_count) >= len(nums) // 2:
        return len(nums) // 2
    else:
        return len(nums_count)