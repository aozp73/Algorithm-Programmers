def solution(order):
    s_assist = []
    cnt = 0 
    
    for num in range(1, len(order)+1): # num : 현재 처리하는 상자 번호
        
        if num != order[cnt]:    # 현재 순서에 맞지 않다면
            s_assist.append(num) # 상자를 보조 컨테이너 벨트에 보관
        else: 
            cnt += 1

        # s_assist의 맨 위 상자가 현재 실어야 하는 순서와 일치하지 않을 때까지 반복
        # 위에서 else문으로 순서가 갱신 되면 아래 while문에 변화 생김
        while s_assist and s_assist[-1] == order[cnt]:
            s_assist.pop()
            cnt += 1 # s_assist의 맨 위 상자가 현재 트럭에 실어야 하는 순서(order[cnt])와 같은지 확인하고,
                     # 같다면, s_assist에서 해당 상자를 꺼내고(pop), cnt 1 증가

    return cnt

print(solution([4, 3, 1, 2, 5]))