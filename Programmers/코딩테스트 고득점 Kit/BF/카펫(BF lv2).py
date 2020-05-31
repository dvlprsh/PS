//Solve
def solution(brown, yellow):
    aliquot = []
    aliquot_set=[]
    #1. yellow 약수 set 구하기
    for v in range(1, yellow+1):
        if yellow % v == 0:
            aliquot.append(v)
    mid=int(len(aliquot)/2)
    if len(aliquot) == 1:
        aliquot_set.append([aliquot[0], aliquot[0]])
    for i in range(mid):
        aliquot_set.append([aliquot[i], aliquot[-i-1]])
        if len(aliquot) % 2 != 0:
            aliquot_set.append([aliquot[mid], aliquot[mid]])

    #2. for 약수_set: brown 구하고 주어진 값과 맞는지 확인
    for set in aliquot_set:
        current_brown = set[0]*2 + set[1]*2 + 4
        if brown == set[0]*2 + set[1]*2 + 4:
            return sorted([set[0]+2, set[1]+2], reverse=True)