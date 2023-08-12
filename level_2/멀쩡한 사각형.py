import math

def solution(W, H):
    # W, H의 최대공약수
    gcd = math.gcd(W, H)
    
    # W, H의 합에서 최대공약수를 뺀 값이 대각선에 의해 잘리는 정사각형의 개수
    unavailable = W + H - gcd
    
    # 전체 정사각형 개수에서 잘리는 정사각형의 개수를 뺀 값 반환
    return W * H - unavailable