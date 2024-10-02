def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    idx1 = 0
    idx2 = 0
    for i in range(len(goal)):
        if cards1[idx1] == goal[i]:
            if idx1 != (len(cards1) - 1):
                idx1 += 1
            continue
        elif cards2[idx2] == goal[i]:
            if idx2 != (len(cards2) - 1):
                idx2 += 1
            continue
        else:
            answer = "No"
        
    return answer