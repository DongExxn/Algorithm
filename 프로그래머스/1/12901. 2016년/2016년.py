def solution(a, b):
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    text = ['FRI', 'SAT', 'SUN' ,'MON' ,'TUE' , 'WED', 'THU']
    
    num = sum(day[:a-1]) + b
    
    idx = num % 7 -1
    
    
    return text[idx]