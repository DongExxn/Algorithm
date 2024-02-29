num = int(input())

distance = list(map(int, input().split()))
weight = list(map(int, input().split()))

total = distance[0] * weight[0] 
min_weight = weight[0] 

for i in range(1, num-1): 
    if min_weight > weight[i]:
        min_weight = weight[i]
    total += min_weight * distance[i]

print(total)    
