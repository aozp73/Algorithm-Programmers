def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()
    answer = 0
    left, right = 0, distance

    while left <= right:
        mid = (left + right) // 2
        del_stones = 0
        pre_stone = 0

        for rock in rocks:
            if rock - pre_stone < mid:  # 현재 가정한 시간보다 돌 사이 거리가 작다면 돌 제거
                del_stones += 1
            else:
                pre_stone = rock

            if del_stones > n:  # 제거된 돌이 주어진 조건 제거개수 n보다 크다면 탈출
                break

        if del_stones > n:  # 제거된 돌이 주어진 조건 제거개수 n보다 크다면, 돌 사이 거리 최소값을 줄임
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer