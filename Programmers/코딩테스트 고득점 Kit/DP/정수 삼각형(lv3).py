#Solve
def solution(triangle):
    memo = []
    for row in triangle:
        new_memo = []
        if not memo:
            memo.append(row[0])
            continue
        for i, v in enumerate(row):
            if i == 0:
                new_memo.append(v + memo[0])
            elif i == len(row)-1:
                new_memo.append(v+memo[-1])
            else:
                new_memo.append(v+ max(memo[i-1], memo[i]))
        memo = new_memo
    return max(memo)