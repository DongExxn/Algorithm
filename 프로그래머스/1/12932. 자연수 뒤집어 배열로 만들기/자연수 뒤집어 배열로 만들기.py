def solution(n):
    answer = []
    
    n = str(n)
    for i in n:
        answer.append(int(i))
    
    return answer[::-1]