# Solve
# 풀이 1 - 풀이2 보다 빠른 풀이
# (테스트 4: 552.34ms, 테스트 5: 290.85ms)
def get_available(memo_dict, memo, count, N):
    new_memo = set()
    for i in range(1, count):
        for v in memo_dict[count-i]:
            for v2 in memo_dict[i]:
                plus = v + v2
                minus = v - v2
                divide = int(v / v2)
                multi = v * v2
                if not plus in memo:
                    new_memo.add(plus)
        
                if not minus in memo and minus > 0:
                    new_memo.add(minus)
              
                if not divide in memo and divide >= 1:
                    new_memo.add(divide)
                 
                if not multi in memo:
                    new_memo.add(multi)
            
    new_memo.add(int(str(N)*count))
    return new_memo

def solution(N, number):
    answer = 1
    memo_dict = { 1: [N]}
    memo = [N]
    while answer < 8:
        if number in memo:
            return answer
        else:
            answer += 1
            memo_dict[answer] = list(get_available(memo_dict, memo, answer, N))
            memo.extend(memo_dict[answer])
    if number in memo:
        return answer
    else:
        return -1

# 풀이 2 - 100점 (but 테스트 4: 1219.17ms, 테스트 5: 576.83ms)
def get_available(memo_dict, memo, count, N):
    new_memo = []
    for i in range(1, count):
        for v in memo_dict[count-i]:
            for v2 in memo_dict[i]:
                plus = v + v2
                minus = v - v2
                divide = int(v / v2)
                multi = v * v2
                if not plus in memo:
                    new_memo.append(plus)
                    memo.append(plus)
                if not minus in memo and minus > 0:
                    new_memo.append(minus)
                    memo.append(minus)
                if not divide in memo and divide >= 1:
                    new_memo.append(divide)
                    memo.append(divide)
                if not multi in memo:
                    new_memo.append(multi)
                    memo.append(multi)
                    
    new_memo.append(int(str(N)*count))
    memo.append(int(str(N)*count))
    return new_memo

def solution(N, number):
    answer = 1
    memo_dict = { 1: [N]}
    memo = [N]
    while answer < 8:
        if number in memo:
            return answer
        else:
            answer += 1
            memo_dict[answer] = get_available(memo_dict, memo, answer, N)

    if number in memo:
        return answer
    else:
        return -1