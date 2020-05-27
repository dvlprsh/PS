# 풀이1- 정확도 100, 효율성 100 (풀이 참고)
def solution(weight):
    max = sum(weight)
    weight.sort()
    _i = 1
    for w in weight:
        if w > _i:
            return _i
        else:
            _i += w

    return max + 1

# 풀이2 -정확도 100, 효율성 0 (시간초과)
from collections import deque
def solution(weight):
    max = sum(weight)
    weight.sort(reverse=True)

    for i in range(1, max):
        if i in weight:
            continue
        _i = i

        for v in weight:
            if v > _i:
                continue
            if _i == 0:
                break
            elif v <= _i:
                _i -= v

        if _i > 0:
            return i


    return max + 1

# 풀이 3 -정확도 100, 효율성 0 (시간초과)
from collections import deque
def solution(weight):
    max = sum(weight)
    weight.sort(reverse=True)
    for i in range(1, max):
        if i in weight:
            continue
        _weight = deque(weight)
        _i = i

        for v in weight:

            if v > _i:
                _weight.popleft()
            elif sum(_weight) == _i:
                break
            elif sum(_weight) > _i:
                _i -= _weight.popleft()
            elif sum(_weight) < _i:
                return i

            if _i == 0:
                break
    return max + 1

# 풀이 4 -정확도 100, 효율성 0 (시간초과)
from collections import deque
def solution(weight):
    max = sum(weight)
    weight.sort(reverse=True)
    for i in range(1, max):
        if i in weight:
            continue
        _i = i
        remain = max
        for v in weight:
            if remain < _i:
                return i
            elif remain < i:
                break
            elif remain == _i:
                break
            elif v > _i:
                remain -= v

            elif remain > _i:
                _i -= v
                remain -= v


            if _i == 0:
                break
    return max + 1

# 풀이 5- 정확도 100, 효율성 0 (시간초과)
from collections import deque
def solution(weight):
    max = sum(weight)
    weight.sort(reverse=True)

    for i in range(1, max):
        if i in weight:
            continue
        _weight = [w for w in weight if w < i]

        _i = i
        remain = sum(_weight)
        for v in _weight:
            if remain < _i:
                return i
            elif remain < i:
                break
            elif remain == _i:
                break
            elif v > _i:
                remain -= v

            elif remain > _i:
                _i -= v
                remain -= v


            if _i == 0:
                break
    return max + 1

