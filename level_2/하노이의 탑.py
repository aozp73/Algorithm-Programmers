def solution(n):
    def hanoi(n, start, middle, end, answer):
        # n이 1일 때는 바로 목표 기둥(end)으로 옮김
        if n == 1:
            answer.append([start, end])
            return
        
        # 1. n-1개 원판을 시작 기둥(start)에서 중간 기둥(middle)로 이동
        hanoi(n-1, start, end, middle, answer)
        # 2. 가장 큰 원판을 시작 기둥(start)에서 목표 기둥(end)으로 이동
        answer.append([start, end])
        # 3. n-1개 원판을 중간 기둥(middle)에서 목표 기둥(end)로 이동 
        hanoi(n-1, middle, start, end, answer)
    
    answer = []
    hanoi(n, 1, 2, 3, answer)

    return answer

