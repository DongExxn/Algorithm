from itertools import combinations

answer = 0
n, m = map(int, input().split())
nums = list(map(int, input().split()))
orders = list(combinations(nums, 3)) # 나올 수 있는 모든 조합 저장

for order in orders:

    s = sum(order)
    if s <= m: # 조건에 해당할 때
        answer = max(s, answer) # M보다 작은 수 중 가장 큰 수
        
print(answer)
