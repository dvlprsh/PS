# Solve
def convert_radix(decimal, n):
    result = ''
    if decimal == 0:
        return '0'
    while decimal >= n:
        remain = decimal % n
        decimal = decimal // n
        result = n_dict[remain] + result
    if decimal < n and decimal > 0:
        result = n_dict[decimal] + result
    return result
def solution(n, t, m, p):
    # n: 진법, t: 미리 구할 숫자, m: 게임 참가 인원, p: 튜브 순서
    answer = ''
    total = ''
    decimal = 0
    global n_dict
    n_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    for i in range(10):
        n_dict[i] = str(i)
    #구해야 하는 숫자 - t * m
    while len(total) < t*m:
        total += convert_radix(decimal, n)
        decimal += 1
    answer = [v for i, v in enumerate(total) if (i+1) % m == (p % m)]
    answer = answer[:t]
    return ''.join(answer)