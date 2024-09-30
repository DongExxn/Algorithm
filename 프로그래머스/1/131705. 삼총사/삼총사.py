import itertools

def solution(number):
    answer = 0
    
    nCr = list(itertools.combinations(number, 3)) 
    
    for i in nCr:
        if sum(i) == 0:
            answer += 1
    return answer