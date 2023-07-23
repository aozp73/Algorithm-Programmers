'math 라이브러리'
# import math

# def solution(arr):
#     answer = arr[0]

#     for n in arr:
#         answer = n * answer // math.gcd(n, answer)

#     return answer

'유클리드 호제법 - 재귀 구현'
# def s_gcd(a, b): # a > b
#     if b == 0:
#         return a
#     else: 
#         return s_gcd(b, a % b)

# def solution(arr):
#     answer = 0
#     answer = arr[0]
#     for n in arr:
#         answer = n * answer // s_gcd(n, answer)

#     return answer

'유클리드 호제법 - 반복문 구현'
# def s_gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a

# def solution(arr):
#     answer = 0
#     answer = arr[0]
#     for n in arr:
#         answer = n * answer // s_gcd(n, answer)

#     return answer