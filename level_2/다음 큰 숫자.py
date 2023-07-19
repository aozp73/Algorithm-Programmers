from collections import Counter

def cnt_binary_one(num):
    temp = ''
    while num > 0:
        temp += str(num % 2)
        num //= 2

    binary_counter = Counter(str(temp))

    return binary_counter['1']

def solution(n):
    
    binary_n = cnt_binary_one(n)
    target = n
    while True:
        target += 1

        if binary_n == cnt_binary_one(target):
            break

    return target

print(solution(78))