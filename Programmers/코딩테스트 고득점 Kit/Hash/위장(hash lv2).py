//Solve
def solution(clothes):
    inventory = {}
    answer = 1
    for cloth in clothes:
        if cloth[1] in inventory:
            inventory[cloth[1]] +=1
        else:
            inventory[cloth[1]] =1

    for i, v in inventory.items():
        answer *= (v+1)

    return answer-1