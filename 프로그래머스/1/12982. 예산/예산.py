def solution(d, budget):
    answer = 0
    
    d.sort()

    for i in range(len(d)):
        if budget >= d[i]:
            answer += 1
            budget -= d[i]
    return answer