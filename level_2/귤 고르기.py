from collections import Counter

def solution(k, tangerine):
    
    s_counter = Counter(tangerine)
    new_list = sorted(list(s_counter.values()), reverse = True)
    
    s_check = 0
    idx = 0
    for idx, num in enumerate(new_list):
        s_check += num
        if s_check >= k:
            idx += 1
            break    

    return idx

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))