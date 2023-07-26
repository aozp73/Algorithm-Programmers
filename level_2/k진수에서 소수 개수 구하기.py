def solution(n, k):
    # 소수 판별 함수
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # n을 k진수로 변환
    converted = ""
    while n > 0:
        n, mod = divmod(n, k)
        converted = str(mod) + converted

    # 0을 기준으로 분리
    candidates = converted.split('0')

    # 소수인지 판별 후 카운트
    cnt = 0
    for num in candidates:
        if num != '' and is_prime(int(num)):
            cnt += 1

    return cnt