# 테스트 케이스 개수 입력
T = int(input())  

for _ in range(T):
    # 높이와 너비 입력
    H, W = map(int, input().split())  
    
    # 그리드 입력
    grid = [input() for _ in range(H)]
    
    # 방문 여부를 저장할 배열 초기화
    visited = [[False] * W for _ in range(H)]
    
    # 방향벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs(x, y):
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == "#":
                    visited[nx][ny] = True
                    stack.append((nx, ny))
    
    # 양 무리 개수를 저장할 변수
    sheep_count = 0
    
    # 그리드 탐색
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "#" and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j)  # 새로운 양 무리 탐색 시작
                sheep_count += 1  # 양 무리 개수 증가
    
    # 결과 출력
    print(sheep_count)
