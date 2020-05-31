# 풀이 참고
def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people) - 1
    while left < right:
        if people[left] + people[right] <= limit:
            answer +=1
            left +=1
            right -=1
        else:
            right -=1
    return len(people)-answer
    
# 시간초과한 풀이 (정확성 100 효율성 0)
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    while people:
        boat = people.pop()
        answer += 1
        
        for i, v in enumerate(people):
            if v + boat <= limit:
                people.pop(i)
                break
    return answer

# 실패한 풀이 (점수 30.0 /100.0)
def solution(people, limit):
    answer = 1
    people.sort(reverse=True)
    current_boat = []
    while people:
        if (people[-1] + sum(current_boat) <= limit) and len(current_boat) < 2:
            current_boat.append(people.pop())
            #print(people)
        else:
            current_boat.clear()
            if len(people) > 0:
                answer+=1
       
    return answer