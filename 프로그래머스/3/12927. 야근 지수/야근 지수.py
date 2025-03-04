import heapq

def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return answer
    
    works = [-w for w in works] # 최소 heap을 사용하기 위해 - 로 변경
    heapq.heapify(works) # heap구조
    
    while n > 0:
        min_value = heapq.heappop(works) 
        heapq.heappush(works, min_value+1) #가장 작은 값에 +1
        n -= 1
    
    for i in works:
        answer += (i ** 2)
    return answer