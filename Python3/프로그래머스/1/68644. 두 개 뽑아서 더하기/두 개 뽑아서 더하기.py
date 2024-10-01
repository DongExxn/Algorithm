import itertools

def solution(numbers):
    answer = []
    
    arr = list(itertools.combinations(numbers, 2))
    
    for i in arr:
        print(sum(i))
        if sum(i) not in answer:
            answer.append(sum(i))
    answer.sort()
    return answer