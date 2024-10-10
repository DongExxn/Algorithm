def solution(n, m, section):
    answer = 0
    index = 0
    position = 0
    section.sort()
    
    if (section[-1] - section[0]) < m:
        answer = 1
    else:
        while index  < len(section):
            answer += 1  
        # 테이프가 덮을 수 있는 범위 계산
            position = section[index] + m - 1
        # 테이프가 덮을 수 있는 범위 안에 있는 위치만큼 index 추가
            while index < len(section) and section[index] <= position:
                index += 1
    return answer