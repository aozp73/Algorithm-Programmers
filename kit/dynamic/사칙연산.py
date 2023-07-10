def solution(arr):
    # n : 숫자 개수
    n = (len(arr) + 1) // 2
    dp_max = [[-float('inf')]*n for _ in range(n)]
    dp_min = [[float('inf')]*n for _ in range(n)]
    
    for i in range(n):
        # dp_max[i][j] : arr의 i번째 숫자부터 j번째 숫자까지 계산했을 때 가능한 최대 값
        # dp_min[i][j] : arr의 i번째 숫자부터 j번째 숫자까지 계산했을 때 가능한 최소 값
        dp_max[i][i] = int(arr[i*2])
        dp_min[i][i] = int(arr[i*2])
        
    for cnt in range(2, n+1):
        for start in range(n-cnt+1):
            end = start + cnt - 1
            for i in range(start, end):
                if arr[i*2+1] == '-':
                    dp_max[start][end] = max(dp_max[start][end], dp_max[start][i] - dp_min[i+1][end])
                    dp_min[start][end] = min(dp_min[start][end], dp_min[start][i] - dp_max[i+1][end])
                else:
                    dp_max[start][end] = max(dp_max[start][end], dp_max[start][i] + dp_max[i+1][end])
                    dp_min[start][end] = min(dp_min[start][end], dp_min[start][i] + dp_min[i+1][end])

    return dp_max[0][n-1]