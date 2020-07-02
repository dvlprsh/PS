# Solve
import math
def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1): # s 를 1 ~ len(s)/2 단위 만큼 잘라서 압축
        piece = ''
        split_arr = [] # split_arr : s를 i 단위만큼 자른 문자열 배열
        for j in range(len(s)):
            piece += s[j] # piece: i길이의 문자열
            if (j+1) % i == 0:
                split_arr.append(piece)
                piece = ''
        split_arr.append(piece)
        zip_string = '' # zip_string : 압축한 문자열
        prev_v = split_arr[0]
        same_count = 1
        # split_arr 순회하며 압축
        for i, v in enumerate(split_arr):
            if i == 0:
                continue
            if prev_v != v:
                if same_count > 1:
                    zip_string += (str(same_count) + prev_v)
                else:
                    zip_string += prev_v
                prev_v = v
                same_count = 1
            else:
                same_count += 1
        if same_count > 1:
            zip_string += (str(same_count) + prev_v)
        else:
            zip_string += prev_v
            
        answer = min(answer, len(zip_string))
    return answer