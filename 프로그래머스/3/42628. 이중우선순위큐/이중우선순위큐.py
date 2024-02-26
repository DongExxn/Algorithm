def solution(operations):
    answer = []
    Answer = []
    
    for i in operations:
        if i[0] == 'I': # I로 시작하는 경우 삽입
            num = i.split(' ')[1]
            answer.append(int(num))
            answer.sort()
        elif i == 'D -1': # 최솟값 제거
            if len(answer) != 0:
                answer.sort()
                answer.remove(answer[0])
            else:
                continue
        else: # 최댓값 제거
            if len(answer) != 0:
                answer.sort()
                answer.pop()
            else:
                continue
    answer.sort()

    if len(answer)==0: #배열 길이가 0일시 반환
        Answer = [0,0]
    else: #배열 길이가 0이 아닐시 최소,최대 반환
        Answer.append(answer[-1])
        Answer.append(answer[0])
    return Answer