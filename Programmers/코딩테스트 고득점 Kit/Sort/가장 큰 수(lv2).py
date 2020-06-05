# 풀이 1 - 풀이 참고
def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers.sort(key= lambda x: x*3, reverse = True)
    return str(int(''.join(numbers)))

# 풀이 2 - 실패 54점 (시간초과)
def solution(numbers):
    answer = ''
    _len = len(numbers)
    numbers = [str(i) for i in numbers]
    for i in reversed(range(_len)):
        for j in range(i):
            if int(numbers[j+1]+numbers[j]) > int(numbers[j]+numbers[j+1]):
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
    for v in numbers:
        answer += v
    return str(int(answer))