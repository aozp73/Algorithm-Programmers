def solution(storey):
    cnt = 0

    while storey:
        remainder = storey % 10
        
        # 6 ~ 9
        if remainder > 5:
            cnt += (10 - remainder)
            storey += 10
        # 0 ~ 4
        elif remainder < 5:
            cnt += remainder
        # 5
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            cnt += remainder
            
        storey //= 10

    return cnt