from collections import deque

def solution(n, edge):
    
    visited = [False] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    distance = [0] * (n + 1)

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    queue = deque([1])
    visited[1] = True

    while queue:
        current = queue.popleft()
        
        for i in graph[current]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[current] + 1
                
    max_distance = max(distance)
    
    return distance.count(max_distance)


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))