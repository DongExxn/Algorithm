from collections import deque

# 상하좌우 탐색용 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수
def bfs(x, y, visited, grid, N, rain_level):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] > rain_level:
                visited[nx][ny] = True
                queue.append((nx, ny))

def max_safe_area(N, grid):
    max_height = max(max(row) for row in grid)  # grid에서 가장 큰 높이 값을 찾음
    max_area = 0

    # 각 강수량에 대해 물에 잠기지 않는 안전 영역 수를 구함
    for rain_level in range(max_height + 1):
        visited = [[False] * N for _ in range(N)]  # 방문 여부 체크
        area_count = 0
        
        # 모든 지점에서 시작하여 안전한 영역을 찾음
        for i in range(N):
            for j in range(N):
                if not visited[i][j] and grid[i][j] > rain_level:
                    bfs(i, j, visited, grid, N, rain_level)
                    area_count += 1
        
        # 최대 안전 영역 개수를 갱신
        max_area = max(max_area, area_count)

    return max_area

# 입력 받기
N = int(input())  # 지역의 크기 N
grid = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(max_safe_area(N, grid))
