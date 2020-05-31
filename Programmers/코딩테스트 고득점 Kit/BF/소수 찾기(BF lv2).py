from itertools import permutations
def solution(numbers):
    answer = 0
    num_list = list(numbers)
    case_list = set()

    for i in range(len(numbers)):
        for value in permutations(num_list, i+1):
            case = int(''.join(list(value)))
            if case != 0 and case != 1:
                case_list.add(case)

    for case in case_list:
        is_prime = True

        for i in range(2, case):
            if case % i == 0:
                is_prime = False
                break
        if is_prime:
            answer+=1

    return answer