def solution(n):
    answer = ''
    num = n // 2
    
    if n % 2 == 0:
        answer += '수박' * num
    else:
        answer += '수박' * num
        answer += '수'
    return answer