from collections import deque

def solution(x, y, n):
    
    visited = [False] * (y + 1)
    q = deque([(x, 0)])

    while q:
        s_num, s_count = q.popleft()

        if s_num == y:
            return s_count

        for s_next_num in [s_num + n, s_num * 2, s_num * 3]:
            if s_next_num <= y and not visited[s_next_num]:
                visited[s_next_num] = True
                q.append((s_next_num, s_count + 1))

    return -1

print(solution(10, 40, 5))