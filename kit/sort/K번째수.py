'슬라이싱, sorted'
# def solution(array, commands):
#     answer = []
#     for i,j,k in commands:
#         answer.append(sorted(array[i-1:j])[k-1])
        
#     return answer


'우선순위 큐, 비효율'
# import heapq

# def solution(array, commands):
#     answer = []

#     for i, j, k in commands:
#         heap = []

#         for m in range(i - 1, j):
#             heapq.heappush(heap, array[m])
            
#         smallest_k = 0
#         for _ in range(k):
#             smallest_k = heapq.heappop(heap)

#         answer.append(smallest_k)
            
#     return answer
