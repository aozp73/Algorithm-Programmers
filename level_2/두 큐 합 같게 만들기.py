from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    # 두 큐의 합 계산
    total_sum_queue1 = sum(queue1)
    total_sum_queue2 = sum(queue2)
    
    # 전체 원소 합이 홀수인 경우, 두 큐의 합을 같게 만들 수 없으므로 -1 반환
    if (total_sum_queue1 + total_sum_queue2) % 2 != 0:
        return -1

    # 작업 횟수를 저장하는 변수
    operation_count = 0

    while True:
        if total_sum_queue1 > total_sum_queue2:
            # queue1의 원소 -> queue2로 옮기기
            transfer_element = queue1.popleft()
            queue2.append(transfer_element)
            total_sum_queue1 -= transfer_element
            total_sum_queue2 += transfer_element
            
        elif total_sum_queue1 < total_sum_queue2:
            # queue2의 원소 -> queue1로 옮기기
            transfer_element = queue2.popleft()
            queue1.append(transfer_element)
            total_sum_queue1 += transfer_element
            total_sum_queue2 -= transfer_element
            
        else:
            # 두 큐의 합이 같아진 경우 루프 종료
            break

        operation_count += 1
        
        # 무한 루프 방지 조건. 큐의 길이의 4배를 넘어가는 작업이 필요하면 -1 반환
        # 4배란 임의의 초과 작업량
        if operation_count == len(queue1) * 4:
            return -1
    
    return operation_count