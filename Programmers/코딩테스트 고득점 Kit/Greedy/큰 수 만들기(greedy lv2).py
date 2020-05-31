//Solve
# 풀이 1 - 정확도 100
# 시간초과 해결 - 배열 slice 대신 deque - popleft() 사용
from collections import deque
def solution(number, k):
    answer = ''
    initial_len = len(number)
    target_len = len(number) - k
    ordered_list= sorted(list(set(number)), reverse = True)
    number = deque(number)

    while initial_len - len(answer) > k:
        max_idx=0
        for idx in range(len(ordered_list)):
            max_number = ordered_list[idx]

            if max_number not in number:
                continue
            else:
                max_idx = number.index(max_number)

                if len(number) - max_idx == target_len:
                    for i in range(max_idx):
                        number.popleft()
                    answer += ''.join(number)
                    return answer
                elif len(number) - max_idx > target_len:
                    for i in range(max_idx):
                        number.popleft()
                    answer+=number.popleft()
                    target_len -= 1
                    break

    return answer

# 풀이 2 - 정확도 91 (case 10번 시간초과)
from collections import deque
import itertools
def solution(number, k):
    answer = ''
    initial_len = len(number)
    target_len = len(number) - k
    ordered_list= sorted(list(set(number)), reverse = True)
    number = deque(number)

    while initial_len - len(answer) > k:
        max_idx=0
        for idx in range(len(ordered_list)):
            max_number = ordered_list[idx]

            if max_number not in number:
                continue
            else:
                max_idx = number.index(max_number)

                if len(number) - max_idx > target_len:
                    number=deque(itertools.islice(number, max_idx, None))
                    answer+=number.popleft()
                    target_len -= 1
                    break
                elif len(number)-max_idx == target_len:
                    number=deque(itertools.islice(number, max_idx, None))
                    answer += ''.join(number)
                    return answer

    return answer