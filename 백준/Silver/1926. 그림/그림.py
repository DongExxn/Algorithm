from collections import deque

# 입력 받기
n, m = map(int, input().split())
canvas = [list(map(int, input().split())) for _ in range(n)]

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 기록용
visited = [[False] * m for _ in range(n)]

# BFS 함수
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    area = 1  # 현재 그림의 넓이

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):  # 네 방향 탐색
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and canvas[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                area += 1
    return area

# 그림 개수와 최대 넓이 계산
picture_count = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if canvas[i][j] == 1 and not visited[i][j]:
            picture_count += 1
            max_area = max(max_area, bfs(i, j))

# 출력
print(picture_count)
print(max_area)
