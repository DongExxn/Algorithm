def solution(phone_number):
    answer = ''
    
    num = len(phone_number)
    
    for i in range(len(phone_number)):
        if i+4 < num:
            answer += '*'
        else:
            answer += phone_number[i]
        
    return answer