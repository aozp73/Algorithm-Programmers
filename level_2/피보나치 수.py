'Top-Down'
import sys
sys.setrecursionlimit(200000)

def solution(n):
    dp = [0, 1] + [-1] * (n-1)

    def fibo(x):
        if dp[x] != -1:
            return dp[x]
        
        dp[x] = (fibo(x - 1) + fibo(x - 2)) % 1234567
        return dp[x]

    return fibo(n)

print(solution(5))

'Bottom-Up'
# def solution(n):
#     s_fibo_list = [0, 1, 1]
#     if n == 2:
#         return s_fibo_list[2] % 1234567
    
#     cnt = 3
#     while True:
#         s_fibo_list.append(s_fibo_list[cnt - 1] + s_fibo_list[cnt - 2])
        
#         if cnt == n:
#             return s_fibo_list[cnt] % 1234567
#         cnt += 1
        
# print(solution(5))