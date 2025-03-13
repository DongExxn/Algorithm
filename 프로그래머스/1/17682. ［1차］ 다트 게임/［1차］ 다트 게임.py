def solution(dartResult):
    answer = 0
    scores = []
    i = 0
    
    while i < len(dartResult):
        # 숫자 판별 (10 고려)
        if dartResult[i].isdigit():
            if i + 1 < len(dartResult) and dartResult[i] == '1' and dartResult[i + 1] == '0':
                score = 10
                i += 1  # '10'이면 인덱스 추가 이동
            else:
                score = int(dartResult[i])
        
        # 보너스 처리
        i += 1
        if dartResult[i] == 'S':
            score **= 1
        elif dartResult[i] == 'D':
            score **= 2
        elif dartResult[i] == 'T':
            score **= 3

        # 옵션 처리
        if i + 1 < len(dartResult) and dartResult[i + 1] in '*#':
            i += 1
            if dartResult[i] == '*':
                score *= 2
                if scores:  # 이전 점수가 있다면 2배로 증가
                    scores[-1] *= 2
            elif dartResult[i] == '#':
                score *= -1

        scores.append(score)
        i += 1  # 다음 문자로 이동

    return sum(scores)
