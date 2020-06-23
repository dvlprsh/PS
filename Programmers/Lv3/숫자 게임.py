# Solve
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    idx1 = 0
    idx2 = 0
    while idx1 < len(A) and idx2 < len(B):
        if B[idx2] > A[idx1]:
            answer += 1
            idx1 += 1
            idx2 += 1
        else:
            idx2 += 1
    return answer