from collections import deque

'큐 활용, O(N^2)'
# def solution(prices):
#     queue_prices = deque([(price, index) for index, price in enumerate(prices)])
#     len_prices = len(prices)
#     answer = []

#     while queue_prices:
#         price, index = queue_prices.popleft()
#         val = 0
#         for p, i in queue_prices:
#             if price > p:
#                 val = i - index
#                 break
#             else:
#                 val = len_prices - index - 1
#         answer.append(val)
#     return answer

'스택 활용, O(N)'
# def solution(prices):
#     answer = [0] * len(prices)
#     stack = []

#     for i, price in enumerate(prices):
#         # stack이 비지 않고, 현재 price가 stack의 마지막 값보다 작다면
#         while stack and price < prices[stack[-1]]:
#             j = stack.pop()
#             answer[j] = i - j
#         stack.append(i)

#     # stack에 남아있는 값들 pop
#     while stack:
#         j = stack.pop()
#         answer[j] = len(prices) - 1 - j

#     return answer