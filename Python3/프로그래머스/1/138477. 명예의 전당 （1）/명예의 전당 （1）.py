from collections import deque

def solution(k, score):
    answer = []
    result = []
    
    for i in range(len(score)):
        if k >= i+1:
            answer.append(score[i])
            result.append(min(answer))
        else:
            answer.sort(reverse = True)
            if score[i] >= answer[-1]:
                answer.pop()
                answer.append(score[i])
                result.append(min(answer))
                answer.sort(reverse=True)  # 내림차순 정렬
            else:
                result.append(min(answer))
    return result