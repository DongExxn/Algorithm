
# 예산
n = int(input())  
requests = list(map(int, input().split()))  
total_budget = int(input())  

max_request = max(requests)

left = 0  
right = max_request 
result = 0  

while left <= right:
    mid = (left + right) // 2 
    
    allocated_budget = 0 

    for request in requests: 
        if request > mid:
            allocated_budget += mid
        else:
            allocated_budget += request 

    # 이분 탐색
    if allocated_budget > total_budget:
        right = mid - 1  
    else:
        result = mid  
        left = mid + 1  

print(result)
