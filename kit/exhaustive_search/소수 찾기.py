'숫자마다 반복 확인'
# from itertools import permutations
# import math

# def isPrime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(math.sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True

# def make_permutations(numbers):
#     res = []
#     for i in range(1, len(numbers) + 1):
#         res.extend(map(int, map(''.join, permutations(numbers, i))))

#     return res

# def solution(numbers):
#     answer = 0
#     num_list = make_permutations(numbers)
#     for num in set(num_list):
#         if isPrime(num):
#             answer += 1
            
#     return answer

# print(solution("17"))

'에라토스테네스의 체'
# from itertools import permutations

# def make_prime_list(n):
#     sieve = [False, False] + [True] * (n - 1)

#     m = int(n ** 0.5)
#     for i in range(2, m + 1):
#         if sieve[i] == False: # 이미 소수가 아님이 판별된 수는 건너뜀
#             continue

#         for j in range(i + i, n + 1, i): # i이후 i의 배수들을 False 판정
#             sieve[j] = False

#     return sieve

# def make_permutations(numbers):
#     res = []
#     for i in range(1, len(numbers) + 1):
#         res.extend(map(int, map(''.join, permutations(numbers, i))))

#     return res

# def solution(numbers):
#     answer = 0
#     num_list = make_permutations(numbers)
#     max_num = max(num_list)
#     print(max_num)
#     prime_list = make_prime_list(max_num)
    
#     for num in set(num_list):
#         if prime_list[num]:
#             answer += 1
            
#     return answer