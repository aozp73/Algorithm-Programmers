'점화식 그대로 구현, 제한조건에 따른 시간 초과'
# def solution(n):
    
#     dp = [0] * (n + 1)
#     dp[1] = 1
#     dp[2] = 2
    
#     for i in range(3, n + 1):
#         dp[i] = dp[i-1] + dp[i-2] 
    
#     return dp[n] % 1000000007

# print(solution(4))

'리스트 검색 없이 변수 활용'
# def solution(n):
#     a, b = 1, 2
    
#     for _ in range(2, n):
#         a, b = b, (a + b) % 1000000007
    
#     return b if n >= 2 else a

# print(solution(4))