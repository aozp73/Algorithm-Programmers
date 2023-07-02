from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    truck_weights = deque(truck_weights)

    while bridge:
        time += 1
        total_weight -= bridge.popleft()

        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                total_weight += truck_weights[0]
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
    return time