from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list)
    for a, b in sorted(tickets, reverse=True):
        routes[a].append(b)
    
    path = []
    def dfs(a):
        while routes[a]:
            dfs(routes[a].pop())
        path.append(a)
    
    dfs('ICN')
    return path[::-1]