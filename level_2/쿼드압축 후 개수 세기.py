def solution(arr):
    
    # 해당 분면의 모든 내부 요소가 같은 숫자인지 체크
    def check(x, y, n):
        init = arr[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != init:  # 같은 수가 아닌 것이 있을 경우 False 반환
                    return False
        return True

    def quad_tree(x, y, n):
        # 만약 범위 내 모든 숫자가 동일하다면, 그 숫자를 반환
        if check(x, y, n):
            return [0, 1] if arr[x][y] else [1, 0] # 조건문에서 1 == True, 0 == False
            
        result = [0, 0] # 현재 분면에서의 0과 1의 개수를 저장할 변수
        half = n // 2   # 현재 분면을 4개의 분면으로 나누기 위해 사용하는 변수
        
        # 해당 범위를 4등분하여 각각 재귀적으로 검사
        for i in range(2):
            for j in range(2):
                sub_result = quad_tree(x + i * half, y + j * half, half)
                result[0] += sub_result[0]
                result[1] += sub_result[1]
        
        return result

    return quad_tree(0, 0, len(arr))
