import collections
def solution(prices):
    answer = [0 for i in range(len(prices))]
    prices = collections.deque(prices)
    for i in range(len(prices)):
        price = prices.popleft()
        for next_price in prices:
            answer[i]+=1
            if price > next_price:
                break
    return answer


'''
#시간초과한 풀이
def solution(prices):
    answer = [0 for i in range(len(prices))]
    for i in range(len(prices)):
        price = prices.pop(0)
        for next_price in prices:
            answer[i]+=1
            if price > next_price:
                break
    return answer
'''