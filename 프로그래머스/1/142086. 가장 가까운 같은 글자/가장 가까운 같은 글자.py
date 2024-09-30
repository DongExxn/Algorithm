def solution(s):
    result = []
    last_position = {}  # 마지막 위치를 저장할 딕셔너리

    for i in range(len(s)):
        if s[i] in last_position:
            # 이전에 등장했던 경우, 그 위치를 result에 추가
            result.append(i - last_position[s[i]])
        else:
            # 처음 등장하는 경우 -1 추가
            result.append(-1)
        
        # 현재 문자의 위치를 업데이트
        last_position[s[i]] = i
    
    return result
