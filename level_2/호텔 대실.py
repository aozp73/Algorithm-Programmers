def time_to_minutes(time_str):
    h, m = map(int, time_str.split(":"))
    return h * 60 + m

def solution(book_time):
    # 각 예약의 시작과 종료 시간을 분 단위로 변환
    book_minutes = [(time_to_minutes(start), time_to_minutes(end) + 10) for start, end in book_time]
    
    # 시작 시간 기준으로 예약들을 정렬
    book_minutes.sort(key=lambda x: x[0])
    
    rooms = []
    for start, end in book_minutes:
        # 각 예약에 대해 이미 사용된 객실 중에서 사용 가능한 객실을 찾음
        found = False
        for i in range(len(rooms)):
            if rooms[i] <= start: # 현재 예약 시간이 방 청소 이후 시간 이후일경우
                rooms[i] = end    # 현재 예약의 종료시간을 해당 방에 갱신
                found = True
                break
        
        # 사용 가능한 객실이 없으면 새로운 객실을 추가로 사용
        if not found:
            rooms.append(end)
    
    return len(rooms)
