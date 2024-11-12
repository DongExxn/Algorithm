dp = [0] * 101

dp[1] = dp[2] = dp[3] = 1

# DP를 이용하여 P(N) 계산
for i in range(4, 101):
    dp[i] = dp[i-2] + dp[i-3]

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N])
