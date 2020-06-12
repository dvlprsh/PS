# Solve
def get_binary(num):
    num = str(bin(num))[2:]
    padding = _n - len(num)
    return '0'*padding + num
def solution(n, arr1, arr2):
    global _n
    _n = n
    answer = []
    arr1 = list(map(lambda x: get_binary(x), arr1))
    arr2 = list(map(lambda x: get_binary(x), arr2))
    for i in range(n):
        row = []
        for v in zip(arr1[i], arr2[i]):
            if v[0] == '1' or v[1] == '1':
                row.append('#')
            else:
                row.append(' ')
        answer.append(''.join(row))
    return answer