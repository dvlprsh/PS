//Solve
# 프로그래머스 테스트 케이스는 100% 통과
# but 댓글에 달린 "BBAABAAAAB", 10 테스트케이스는 통과못함
def solution(name):
    closed_list = [] #조작 완료:True, 조작 미완성: False
    answer = 0
    vertical_count = []
    idx = 0
    next_idx = 0

    for char in list(name):
        if char == 'A':
            closed_list.append(True)
        else:
            closed_list.append(False)
        up_count = ord(char) - ord('A')
        down_count = ord('A') - ord(char) + 26
        vertical_count.append(min(up_count, down_count))

    while False in closed_list:
        min_width = len(name)
        for i in range(len(closed_list)):
            if not closed_list[i]:
                right_count = abs(i - idx)
                left_count = idx - i + len(list(name))
                width = min(right_count, left_count)
                # Todo: width == min_width 인 경우 어떤 idx 선택할지
                if width < min_width:
                    min_width = width
                    next_idx = i

        answer += min_width
        answer += vertical_count[next_idx]
        closed_list[next_idx] = True
        idx = next_idx
    return answer