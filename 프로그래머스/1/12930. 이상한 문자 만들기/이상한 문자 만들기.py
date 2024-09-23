def solution(s):
    answer = []
    
    for i in s.split(' '):
        temp_list = []  # 각 단어마다 새로 리스트를 초기화
        for j in range(len(i)):
            if j % 2 == 0:
                temp_list.append(i[j].upper())
            else:
                temp_list.append(i[j].lower())  # 소문자로 변환해야 합니다
        answer.append(''.join(temp_list))
    
    return ' '.join(answer)
