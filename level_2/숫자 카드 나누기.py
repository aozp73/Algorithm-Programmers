def solution(arrayA, arrayB):
    answer = 0
    
    # arrayA의 첫 번째 원소로 최대공약수 초기화
    gcdA = arrayA[0]
    # arrayB의 첫 번째 원소로 최대공약수 초기화
    gcdB = arrayB[0]
    
    # arrayA의 나머지 원소들에 대해 최대공약수 계산
    for n in arrayA[1:]:
        gcdA = gcd(n, gcdA)
        
    # arrayB의 나머지 원소들에 대해 최대공약수 계산
    for n in arrayB[1:]:
        gcdB = gcd(n, gcdB)
        
    # 첫 번째 조건
    if not any(n % gcdB == 0 for n in arrayA):
        answer = max(answer, gcdB)
    
    # 두 번째 조건
    if not any(n % gcdA == 0 for n in arrayB):
        answer = max(answer, gcdA)
        
    return answer

# 최대공약수 (유클리드 호제법)
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)
