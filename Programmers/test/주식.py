from collections import deque
def solution(prices):
    answer = []
    c_prices = deque(prices)
    for i, v1 in enumerate(prices):
        time = 0
        c_prices.popleft()
        #for v2 in prices[i+1:]:
        for v2 in c_prices:
            time +=1
            if v2 < v1:
                break
        answer.append(time)
    return answer