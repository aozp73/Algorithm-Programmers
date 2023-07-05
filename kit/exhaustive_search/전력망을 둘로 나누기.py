# from itertools import combinations
# from collections import Counter

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# def solution(n, wires):
    
#     res = int(1e9)
#     for wire_case in combinations(wires, n - 2):
#         parent = [0] * (n + 1) 
#         for i in range(1, n + 1):
#              parent[i] = i
        
#         for a, b in wire_case:
#             union_parent(parent, a, b)
            
#         for i in range(1, n + 1):
#             parent[i] = find_parent(parent, i)
            
#         values = list(Counter(parent[1:]).values())
        
#         cnt = abs(values[0]-values[1])
#         res = min(res, cnt)

#     return res

# print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))