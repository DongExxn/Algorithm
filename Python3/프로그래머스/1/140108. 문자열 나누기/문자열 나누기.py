def solution(s):
    answer = 0
    a = 0
    b = 0
    for i in s:
        if a == b:
            answer += 1
            S = i
        if S == i:
            a += 1
        else:
            b += 1

    return answer