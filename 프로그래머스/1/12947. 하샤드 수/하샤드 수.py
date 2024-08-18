def solution(x):
    answer = True
    sum = 0
    x = str(x)
    
    for i in x:
        sum += int(i)
        
    x = int(x)
    
    if x % sum != 0:
        answer = False
    return answer