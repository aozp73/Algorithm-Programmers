from collections import Counter

def solution(topping):
    answer = 0
    s_left_counter = Counter()
    s_right_counter = Counter(topping)

    for i in range(len(topping)-1):
        s_left_counter[topping[i]] += 1
        s_right_counter[topping[i]] -= 1
        
        if s_right_counter[topping[i]] == 0:
            del s_right_counter[topping[i]]
            
        if len(s_left_counter) == len(s_right_counter):
            answer += 1
            
    return answer