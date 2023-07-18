from collections import Counter

def solution(s):
    s_remove_cnt = 0
    s_change_cnt = 0
    s = list(map(int, s))

    while True:
        s_counter = Counter(s)
        s_remove_cnt += s_counter[0]

        s = [s_num for s_num in s if s_num != 0]
        s_change_cnt += 1

        if len(s) == 1 and s[0] == 1:
            break

        a = len(s)
        s = []
        while a > 0:
            s.append(a % 2)
            a = a // 2

        s.sort(reverse = True)

    return [s_change_cnt, s_remove_cnt]

print(solution("110010101001"))
