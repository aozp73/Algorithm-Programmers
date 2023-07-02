from collections import deque

def solution(priorities, location):

    queue = deque([(priority, index) for index, priority in enumerate(priorities)])
    cnt = 0
    
    while queue:
        priority, index = queue.popleft()
        
        if any(priority < p for p, _ in queue):
            queue.append((priority, index))
        else:
            cnt += 1
            if index == location:
                return cnt

    return -1
