from collections import deque

def solution(record):

    queue = deque([])
    s_change_list = {}
    
    for str in record:
        if "Leave" in str.split()[0]:
            s_command, s_id = str.split()
            queue.append(('Leave', s_id))
        else:
            s_command, s_id, s_nickname = str.split()
            if "Change" in str:
                s_change_list[s_id] = s_nickname
            else:
                s_change_list[s_id] = s_nickname
                queue.append(('Enter', s_id))
    
    answer = []
    while queue:
        data = queue.popleft()
        check_nickname = s_change_list[data[1]]
        if data[0] == "Enter":
            answer.append(check_nickname+"님이 들어왔습니다.")
        else:
            answer.append(check_nickname+"님이 나갔습니다.")
    return answer