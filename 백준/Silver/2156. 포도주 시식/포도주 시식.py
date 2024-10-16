def max_wine(n, wine):
    if n == 1:
        return wine[0]
    elif n == 2:
        return wine[0] + wine[1]
    
    dp = [0] * n
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(wine[0] + wine[2], wine[1] + wine[2], wine[0] + wine[1])
    
    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])
    
    return dp[n-1]

# 입력 처리
n = int(input())
wine = [int(input()) for _ in range(n)]

# 결과 출력
print(max_wine(n, wine))
