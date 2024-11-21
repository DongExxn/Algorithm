# 도영이가 만든 맛있는 음식

from itertools import combinations

n = int(input())
ingredients = [tuple(map(int, input().split())) for _ in range(n)]

min_diff = float('inf')

for r in range(1, n + 1):
    for combo in combinations(ingredients, r):
        sour = 1  # 신맛
        bitter = 0  # 쓴맛
        
        for s, b in combo:
            sour *= s
            bitter += b
        
        diff = abs(sour - bitter)
        
        if diff < min_diff:
            min_diff = diff

print(min_diff)
