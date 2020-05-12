import sys
import math
print("Debug messages...", file=sys.stderr)
def get_char_score(char):
    letter_scores = {'a' : 1, 'b' : 3, 'c' : 3, 'd': 2, 'e' : 1, 'f' : 4,
     'g' : 2, 'h' : 4, 'i': 1, 'j' : 8, 'k' : 5, 'l': 1, 'm' : 3, 'n': 1, 'o' : 1, 'p' : 3,
     'q' : 10, 'r': 1, 's' : 1, 't' : 1, 'u' : 1, 'v' : 4, 'w' : 4, 'x' : 8, 'y' : 4, 'z' : 10}
    return letter_scores[char]

def get_word_score(word):
    word_score=0
    for char in word:
        word_score += get_char_score(char)

    return word_score

def is_word_feasible(word, letters):
    for char in word:
        if word.count(char) > letters.count(char):
            return False
    return True

n = int(input())
dictionary= [input() for i in range(n)]
print(dictionary, file=sys.stderr)
letters = input()
max_score = 0
max_scored_word = ""
for word in dictionary:
    if is_word_feasible(word, letters):
        word_score=get_word_score(word)
        if word_score > max_score:
            max_score=word_score
            max_scored_word=word


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

print(max_scored_word)
