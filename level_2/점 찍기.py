def solution(k, d):
    count = 0
    
    for x in range(0, d+1, k):
        # y^2 + x^2 <= d^2  => y <= sqrt(d^2 - x^2)
        max_y = int((d**2 - x**2) ** 0.5)  # 가능한 y의 최댓값
        count += (max_y // k + 1)  # x축 점도 고려하기 위해 + 1 
    return count
