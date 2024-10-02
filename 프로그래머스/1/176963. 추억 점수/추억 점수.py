def solution(name, yearning, photo):
    answer = [0 for _ in range(len(photo))]

    dict = {}
    
    for i in range(len(name)):
        dict[name[i]] = yearning[i]

    for i in range(len(photo)):
        for j in photo[i]:
            if j in dict:
                answer[i] += dict[j]

    return answer