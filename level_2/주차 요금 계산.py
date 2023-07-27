import math
def solution(fees, records):
    # 주차 시간 기록용
    car_record_minute = dict()
    # 현재 주차되어 있는 차 확인용
    parked_cars = dict()

    for record in records:
        time, car_num, status = record.split()
        hh, mm = map(int, time.split(':'))
        total_minutes = hh*60 + mm

        if status == "IN":
            parked_cars[car_num] = total_minutes
        elif status == "OUT":
            parking_time = total_minutes - parked_cars[car_num]
            
            # 오늘 처음 온 차가 아니라면,
            if car_num in car_record_minute:
                car_record_minute[car_num] += parking_time
            # 오늘 처음 온 차라면
            else:
                car_record_minute[car_num] = parking_time
                
            del parked_cars[car_num]

    # 오늘 OUT하지 않은 차량 처리
    for car_num, in_time in parked_cars.items():
        out_time = 23*60 + 59
        parking_time = out_time - in_time
        if car_num in car_record_minute:
            car_record_minute[car_num] += parking_time
        else:
            car_record_minute[car_num] = parking_time

    answer = []
    for car_num in sorted(car_record_minute.keys()):
        # 기본 시간 이용 차량
        if car_record_minute[car_num] <= fees[0]:
            answer.append(fees[1])
        # 기본 시간 이용 초과 차량
        else:
            answer.append(fees[1] + math.ceil((car_record_minute[car_num] - fees[0]) / fees[2]) * fees[3])

    return answer