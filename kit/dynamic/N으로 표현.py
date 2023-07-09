from collections import defaultdict

def solution(N, number):
    
    dp = defaultdict(set)

    for i in range(1, 10):
        dp[i].add(int(str(N) * i))
        
        for j in range(1, i):
            for left_num in dp[j]:
                for right_num in dp[i-j]:
                    dp[i].add(left_num + right_num)
                    dp[i].add(left_num - right_num)
                    dp[i].add(left_num * right_num)
                    if right_num != 0: dp[i].add(left_num // right_num)  

        if number in dp[i]: return i 
        
    return -1 


print(solution(5, 12))
