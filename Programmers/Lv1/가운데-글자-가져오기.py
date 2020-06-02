def solution(s):
    _l = len(s)
    _mid = int(_l /2)
    if len(s) % 2 == 0:
        return s[_mid-1:_mid+1]
    else:
        return s[_mid]