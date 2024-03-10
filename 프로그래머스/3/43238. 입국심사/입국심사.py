def solution(n, times):
    start, end = 1, min(times) * n
    
    while start <= end:
        cnt = 0 
        
        mid = (start + end) // 2 
        
        for time in times:
            cnt += mid // time
            
        if cnt < n:
            start = mid + 1
        else:
            end = mid - 1 
    return start