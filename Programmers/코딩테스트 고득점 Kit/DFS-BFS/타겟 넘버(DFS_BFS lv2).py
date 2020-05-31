def solution(numbers, target):
    answer = 0
    sum = 0
    idx = 0
    def get_target_count(idx, sum, count):
        if idx == len(numbers):
            if sum  == target:
                return count +1
            else:
                return count
        return get_target_count(idx + 1, sum + numbers[idx], count) + get_target_count(idx + 1, sum - numbers[idx], count)

    answer=get_target_count(idx, sum, answer)
    return answer