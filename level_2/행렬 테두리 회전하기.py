def rotate(matrix, query):
    x1, y1, x2, y2 = query
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    temp = matrix[x1][y1]
    minimum = temp

    # ↑ (왼쪽 row)
    for i in range(x1, x2):
        matrix[i][y1] = matrix[i+1][y1]
        minimum = min(minimum, matrix[i][y1])
    # <-- (아래쪽 column)
    for i in range(y1, y2):
        matrix[x2][i] = matrix[x2][i+1]
        minimum = min(minimum, matrix[x2][i])

    # ↓ (오른쪽 row)
    for i in range(x2, x1, -1):
        matrix[i][y2] = matrix[i-1][y2]
        minimum = min(minimum, matrix[i][y2])
    # --> (위쪽 column)
    for i in range(y2, y1, -1):
        matrix[x1][i] = matrix[x1][i-1]
        minimum = min(minimum, matrix[x1][i])

    matrix[x1][y1+1] = temp

    return minimum

def solution(rows, columns, queries):
    matrix = [[(i * columns) + j + 1 for j in range(columns)] for i in range(rows)]
    answer = [rotate(matrix, query) for query in queries]

    return answer
