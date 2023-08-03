def solution(sequence, k):
    min_length = 1e9 # 부분 수열의 최소 길이 저장
    answer = [0, 0]  # 최소 길이 부분 수열의 시작과 끝 인덱스를 저장할 변수
    
    sum = 0 # 부분 수열의 합을 저장하는 변수    
    l = 0 # l: 부분 수열의 시작점, r: 끝점
    r = 0

    while True:
        if sum < k: # 부분 수열의 합 < k
            if r == len(sequence): # r이 수열의 끝에 도달했다면 반복문을 종료
                break
            
            sum += sequence[r] # 부분 수열의 합에 현재 r 위치의 값을 더함
            r += 1 
            
        else: # 부분 수열의 합 >= k 
            if sum == k and r - l < min_length: # 합이 k와 같고 현재 부분 수열의 길이가 최소 길이보다 작다면,
                min_length = r - l  # 최소 길이 업데이트
                answer = [l, r - 1] # 시작과 끝 인덱스 업데이트
                
            sum -= sequence[l] # l 위치의 값을 부분 수열의 합에서 뺌
            l += 1         

    return answer 
