# Solve
import re
def solution(files):
    answer = []
    # _files = [[파일명, head, number]]
    _files = []
    pattern = r"([0-9])+"
    repatter = re.compile(pattern)
    for v in files:
        n_match = re.search(pattern, v)
        start_idx, end_idx = n_match.span()
        _files.append([v, v[0:start_idx].lower(),int(v[start_idx:end_idx])])
    _files.sort(key= lambda x: (x[1], x[2]))
    answer = [i[0] for i in _files]
    return answer