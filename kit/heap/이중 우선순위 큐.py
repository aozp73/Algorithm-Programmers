'최대 힙, 최소 힙 동기화'
# import heapq

# def solution(operations):
#     max_priority_heap = []
#     min_priority_heap = []

#     for operation in operations:
#         op, num = operation.split()
#         num = int(num)
        
#         if op == "I":
#             heapq.heappush(max_priority_heap, -num)
#             heapq.heappush(min_priority_heap, num)
#         elif num == 1:
#             if max_priority_heap:
#                 max_value = -heapq.heappop(max_priority_heap)
#                 min_priority_heap.remove(max_value)
#         else:
#             if min_priority_heap:
#                 min_value = heapq.heappop(min_priority_heap)
#                 max_priority_heap.remove(-min_value)

#     if not max_priority_heap or not min_priority_heap:
#         return [0, 0]
#     else:
#         return [-heapq.heappop(max_priority_heap), heapq.heappop(min_priority_heap)]


'최대 힙, 최소 힙 교집합'
# import heapq

# def solution(operations):
#     max_priority_heap = []
#     min_priority_heap = []
    
#     for operation in operations:
#         if operation.startswith('I '):
#             new_operation = operation.replace('I ', '')
#             heapq.heappush(max_priority_heap, -int(new_operation))
#             heapq.heappush(min_priority_heap, int(new_operation))
#         elif operation.startswith("D 1"):
#             if max_priority_heap: 
#                 heapq.heappop(max_priority_heap)
#         elif operation.startswith("D -1"):
#             if min_priority_heap:  
#                 heapq.heappop(min_priority_heap)
            
#     max_val = int(-1e9)
#     min_val = int(1e9)
#     answer = []
#     for val in max_priority_heap:
#         if -val in min_priority_heap:
#             max_val = max(max_val, -val)
#             min_val = min(min_val, -val)
    
#     if max_val == int(-1e9) and min_val == int(1e9):
#         return [0, 0]
#     else:
#         return [max_val, min_val]