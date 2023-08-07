import heapq

def dijkstra(n, graph):
    distances = [float('inf')] * (n + 1) # 최단 거리 테이블
    distances[1] = 0
    
    queue = [] # 우선순위 큐 활용
    heapq.heappush(queue, [0, 1])  # [거리, 노드 번호]. 거리가 우선 순위

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance: 
            continue

        for adj, weight in graph[current_node]: # 연결된 노드, 가중치
            distance = current_distance + weight
            if distance < distances[adj]:
                distances[adj] = distance
                heapq.heappush(queue, [distance, adj])

    return distances

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    
    for r in road: # 연결 정보 저장 (인접 리스트)
        graph[r[0]].append([r[1], r[2]])
        graph[r[1]].append([r[0], r[2]])

    distances = dijkstra(N, graph)
    
    count = 0
    for distance in distances:
        if distance <= K: # 주어진 K보다 작은 마을만 cnt
            count += 1

    return count