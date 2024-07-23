def solution(seoul):
    answer = '김서방은 '
    
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer += str(i)
            
    return answer + '에 있다'