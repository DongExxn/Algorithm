def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        if (int(food[i]) // 2) != 0:
            answer += str(i) * (int(food[i]) // 2)
    
    reverse = answer[::-1]
    answer += '0'
    
    answer += reverse
    return answer