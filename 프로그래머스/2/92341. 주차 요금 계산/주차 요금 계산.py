import math

def calculate(time):
    # 10:00 -> 600 형태로 변환
    si, bun = map(int, time.split(":"))
    result = (si*60) + bun
    return result
    
def calculate_fee(parking_time, fees):
    # 주차 요금 계산
    base_time, base_fee, unit_time, unit_fee = fees
    if parking_time <= base_time:
        return base_fee
    return base_fee + math.ceil((parking_time - base_time) / unit_time) * unit_fee
    
def solution(fees, records):
    answer = []
    result_list = {}  # 차량별 총 주차 시간
    record_list = {}  # 차량별 마지막 입차 시간

    
    for i in range(len(records)):
        time, num, types = records[i].split(" ")
        full_time = calculate(time)
        
        if types == 'IN':
            record_list[num] = full_time  # 입차 시간 저장
        else:
            # OUT일 시 총 주차 시간 업데이트 후 기록 삭제
            result_list[num] = result_list.get(num, 0) + (full_time - record_list[num])
            del record_list[num]
    
    # 아직 출차되지 않은 차량 23:59 기준으로 계산
    for num, full_time in record_list.items():
        result_list[num] = result_list.get(num, 0) + (calculate("23:59") - full_time)
    
    # 차량 번호 기준 정렬 후 요금 계산
    result = []
    for num in sorted(result_list.keys()):
        result.append(calculate_fee(result_list[num], fees))
        
    return result