def solution(n):
    answer = 0
        
    for i in range(1, n//2+2):
        if i * i == n:
            return (i + 1) * (i + 1)
    return -1