from collections import deque

# 상하좌우 이동을 위한 방향 배열
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y, team_color, grid, visited):
    # BFS를 사용하여 하나의 팀을 찾아 팀 크기 계산
    queue = deque([(x, y)])
    visited[x][y] = True
    team_size = 1  # 현재 팀 크기

    while queue:
        cx, cy = queue.popleft()

        # 상하좌우 4방향으로 탐색
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            # 범위 내에 있고, 방문하지 않았으며 같은 팀이라면
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visited[nx][ny] and grid[nx][ny] == team_color:
                visited[nx][ny] = True
                queue.append((nx, ny))
                team_size += 1
    
    return team_size

# 입력 받기
N, M = map(int, input().split())  # 전쟁터 크기 N, M
grid = [input().strip() for _ in range(M)]  # 전쟁터 상태
visited = [[False] * N for _ in range(M)]  # 방문 여부 체크

# 아군과 적군의 위력
white_power = 0
blue_power = 0

# 전쟁터에서 각 팀을 찾아서 위력 계산
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            # 현재 팀 색상
            team_color = grid[i][j]
            team_size = bfs(i, j, team_color, grid, visited)

            # 위력은 팀 크기의 제곱
            if team_color == 'W':
                white_power += team_size ** 2
            else:
                blue_power += team_size ** 2

# 결과 출력
print(white_power, blue_power)
