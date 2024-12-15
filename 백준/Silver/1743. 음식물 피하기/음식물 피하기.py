from collections import deque

# 입력 받기
n, m, k = map(int, input().split())
grid = [[0] * m for _ in range(n)]

# 음식물 좌표 입력
for _ in range(k):
    r, c = map(int, input().split())
    grid[r - 1][c - 1] = 1

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    size = 1  # 현재 음식물 크기

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):  # 상하좌우 탐색
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                size += 1
    return size

# 방문 기록용
visited = [[False] * m for _ in range(n)]

# 최대 음식물 크기 찾기
max_size = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and not visited[i][j]:
            max_size = max(max_size, bfs(i, j))

# 출력
print(max_size)
