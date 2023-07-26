def solution(str1, str2):
    s_new_str1 = []
    s_new_str2 = []
    
    for i in range(len(str1) - 1):
        s_str = str1[i:i+2].upper()
        if s_str.isalpha():
            s_new_str1.append(s_str)
        
    for i in range(len(str2) - 1):
        s_str = str2[i:i+2].upper()
        if s_str.isalpha():
            s_new_str2.append(s_str)

    s_set_str1 = set(s_new_str1)
    s_set_str2 = set(s_new_str2)

    intersection = s_set_str1 & s_set_str2  # 교집합
    union = s_set_str1 | s_set_str2         # 합집합

    cnt1 = sum(min(s_new_str1.count(x), s_new_str2.count(x)) for x in intersection)
    cnt2 = sum(max(s_new_str1.count(x), s_new_str2.count(x)) for x in union)

    if cnt2 == 0:
        return 65536

    return int(cnt1 * 65536 / cnt2)