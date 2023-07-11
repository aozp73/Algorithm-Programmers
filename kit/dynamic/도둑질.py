def solution(money):
    n = len(money)

    # 첫번째 집을 털 경우
    dp1 = [0] * (n - 1)
    # 첫번째 집을 털지 않을 경우
    dp2 = [0] * (n)

    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    # 첫번째 집을 털 경우 마지막 집은 털지 못함 (n - 1)
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    # 첫번째 집을 털지 않을 경우 마지막 집 털 수 있음 (n)
    dp2[1] = money[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    return max(max(dp1), max(dp2))