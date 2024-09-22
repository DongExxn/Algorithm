def solution(price, money, count):
    array = []

    for i in range(1, count+1):
        array.append(i*price)
        
    answer = sum(array) - money
    
    if answer > 0:
        return answer
    else:
        return 0