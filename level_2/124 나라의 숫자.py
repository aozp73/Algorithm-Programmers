def solution(n):
    num = ['1','2','4']
    answer = ''

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3
    return answer

print(solution(4)) # 1 2 4 11 12 14 21 22 24 41