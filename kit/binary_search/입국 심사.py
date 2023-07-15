'while'
# def solution(n, times):
#     answer = 0
#     left = 1
#     right = max(times) * n

#     while left <= right:
#         mid = (left + right) // 2
#         people = 0
        
#         for i in times:
#             people += mid // i  # 각 심사관마다, 주어진 시간(mid) 동안 몇 명의 사람을 심사할 수 있는지 계산
#             if people >= n:  
#                 break

#         if people >= n:   # 모든 사람을 심사할 수 있는 경우
#             answer = mid
#             # 시간 조금 더 줄임 (구하고자 하는 값 : 최소 시간)
#             right = mid - 1
#         elif people < n:  # 모든 사람을 심사할 수 없는 경우
#             # 시간 조금 더 늘림
#             left = mid + 1

#     return answer

'재귀 함수'
# def solution(n, times):
#     def binary_search(n, times, left, right):
#         if left > right:
#             return right + 1

#         mid = (left + right) // 2
#         people = sum(mid // time for time in times)

#         if people >= n:
#             return binary_search(n, times, left, mid - 1)
#         else:
#             return binary_search(n, times, mid + 1, right)
#     return binary_search(n, times, 1, max(times) * n)
