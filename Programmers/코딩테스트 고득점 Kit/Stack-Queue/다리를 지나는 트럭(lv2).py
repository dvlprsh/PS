//Solve
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_num = len(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])

    complete = 0
    c_weight = 0
    while complete < truck_num:
        answer+=1
        truck = bridge.popleft()
        if truck !=0:
            complete += 1
            c_weight -= truck
        if truck_weights and c_weight + truck_weights[0] <= weight:
            w = truck_weights.pop(0)
            c_weight += w
            bridge.append(w)
        else:
            bridge.append(0)
                  
    return answer

# 시간초과
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_num = len(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    complete = []
    while len(complete) < truck_num:
        answer+=1
        truck = bridge.popleft()
        if truck !=0:
            complete.append(truck)
        if truck_weights and sum(bridge) + truck_weights[0] <= weight:
            
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
                  
    return answer