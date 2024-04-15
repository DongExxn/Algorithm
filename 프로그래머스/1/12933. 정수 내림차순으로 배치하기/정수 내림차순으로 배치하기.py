def solution(n):
    answer = []
    result = []
    n = str(n)
    
    for i in n:
        answer.append(int(i))
    answer.sort(reverse=True)
    
    for i in answer:
        result.append(str(i))
    result = int(''.join(result))
    return result