# 210216 https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length #다리를 건너고있는 트럭
    
    from collections import deque
    truck_weights = deque(truck_weights)
    
    while len(bridge) != 0:
        time += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
        
    return time

#testcode
print(solution(2,10,[7,4,5,6])) #8
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10])) #110