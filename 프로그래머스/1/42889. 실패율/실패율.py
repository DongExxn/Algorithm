def solution(N, stages):
    answer = []
    
    stage_count = {}  
    num = len(stages)
    # 스테이지 별로 플레이어 수를 세기
    for i in stages:
        if i in stage_count:
            stage_count[i] += 1
        else:
            stage_count[i] = 1
     
    # 실패율을 저장할 딕셔너리
    failure_rates = {}
    temp_players = num  # 전체 사용자 수
    
    for stage in range(1, N + 1):
        if stage in stage_count:  # 해당 스테이지에 도전한 사용자 수가 있는 경우
            fail_count = stage_count[stage]  # 해당 스테이지에서 클리어하지 못한 사용자 수
            failure_rate = fail_count / temp_players  # 실패율 계산
            failure_rates[stage] = failure_rate  # 실패율을 딕셔너리에 저장
            temp_players -= fail_count  # 다음 스테이지를 위한 총 사용자 수 감소
        else:
            failure_rates[stage] = 0  # 도전자가 없는 경우 실패율은 0
    
    # 실패율 기준으로 내림차순 정렬, 실패율이 같을 경우 스테이지 번호 오름차순
    sorted_stages = sorted(failure_rates.items(), key=lambda x: (-x[1], x[0]))
    #print(sorted_stages) # [(3, 0.5), (4, 0.5), (2, 0.42857142857142855), (1, 0.125), (5, 0)]
    # 결과 리스트에 스테이지 번호 추가
    answer = [stage for stage, rate in sorted_stages]

    return answer