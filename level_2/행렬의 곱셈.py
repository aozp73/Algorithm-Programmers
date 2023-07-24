def solution(arr1, arr2):
    arr1_row    = len(arr1)
    arr1_column = len(arr1[0])
    
    arr2_row    = len(arr2)
    arr2_column = len(arr2[0])
    
    answer = [[0] * arr2_column for _ in range(arr1_row)]
    print(answer)
    for i in range(arr1_row):
        for j in range(arr2_column):
            for k in range(arr2_row): # arr1_column == arr2_row
                answer[i][j] += (arr1[i][k] * arr2[k][j])
                
    return answer

solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4, 3], [2, 4, 1], [3, 1, 1]])