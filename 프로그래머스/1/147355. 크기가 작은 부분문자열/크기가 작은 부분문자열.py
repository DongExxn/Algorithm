def solution(t, p):
    answer = 0
    
    num = len(p)
    
    for i in range(len(t)-num+1):
        new = int(t[i:i+num])
        if new <= int(p):
            answer += 1
    return answer