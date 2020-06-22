# Solve
def solution(n, words):
    used_words = []
    for i, v in enumerate(words):
        if i == 0:
            used_words.append(v)
            continue
        elif v[0] != words[i-1][-1] or v in used_words:
            return [i % n + 1, i // n +1 ]
        used_words.append(v)    
    return [0, 0]