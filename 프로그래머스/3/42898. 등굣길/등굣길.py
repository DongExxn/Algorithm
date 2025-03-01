def solution(m, n, puddles):
    MOD = 1000000007
    arr = [[0] * (m+1) for i in range(n+1)]
    
    arr[1][1] = 1  # 시작 위치
    
    for x, y in puddles:
        arr[y][x] = -1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
                
            if arr[i][j] == -1:
                arr[i][j] = 0
            else:
                # 위쪽에서 오는 경우
                if i > 1:
                    from_top = arr[i - 1][j]
                else:
                    from_top = 0  # 위쪽이 없으면 0

                # 왼쪽에서 오는 경우
                if j > 1:
                    from_left = arr[i][j - 1]
                else:
                    from_left = 0  # 왼쪽이 없으면 0

                # 두 방향에서 오는 값을 더해서 MOD 연산
                arr[i][j] = (from_top + from_left) % MOD
    return arr[n][m]