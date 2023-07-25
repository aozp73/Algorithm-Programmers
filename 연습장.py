def solution(s):
    # s : {{4, 2, 3},{3},{2, 3, 4, 1},{2, 3}}
    answer = []
    # splitted : ['4, 2, 3', '3', '2, 3, 4, 1', '2, 3']
    splitted = s[2:-2].split("},{") 

    # spl_split : [['4', ' 2', ' 3'], ['3'], ['2', ' 3', ' 4', ' 1'], ['2', ' 3']]
    spl_split = [spl.split(',') for spl in splitted]

    # splitted2 : [['3'], ['2', ' 3'], ['4', ' 2', ' 3'], ['2', ' 3', ' 4', ' 1']]
    splitted2 = sorted(spl_split, key=lambda x:len(x))

    answer.append(int(splitted2[0][0]))   
    for i in range(1, len(splitted2)):    
        for s in splitted2[i]:             
            if s not in splitted2[i-1]:
                answer.append(int(s))
                break

    return answer

print(solution("{{4, 2, 3},{3},{2, 3, 4, 1},{2, 3}}"))