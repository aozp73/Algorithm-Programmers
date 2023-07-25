from collections import Counter

def solution(want, number, discount):

    s_check = {}
    s_cnt = 0
    for i in range(len(want)):
        s_check[want[i]] = number[i]
        
    for i in range(len(discount) - 10 + 1):
        if s_check == Counter(discount[i:i+10]):
            s_cnt += 1 

    return s_cnt

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], 
               ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))