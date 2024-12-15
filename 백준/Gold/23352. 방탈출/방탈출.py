from collections import deque

# 상하좌우 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수 (최단 경로 계산)
def bfs(start_x, start_y, n, m, grid):
    visited = [[False] * m for _ in range(n)]
    distance = [[-1] * m for _ in range(n)]
    
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    distance[start_x][start_y] = 0
    
    # BFS 탐색
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
    
    # distance 배열 반환
    return distance

# 가장 긴 경로의 시작과 끝에 적힌 숫자 합을 구하는 함수
def find_max_password(n, m, grid):
    max_length = 0
    max_sum = 0
    
    # 모든 방에서 BFS를 수행
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0:  # 갈 수 있는 방인 경우
                # 해당 방에서 BFS를 수행하여 최단 경로를 구한다
                distance = bfs(i, j, n, m, grid)
                
                # BFS 후, 가장 멀리 있는 방을 찾아야 한다
                for x in range(n):
                    for y in range(m):
                        if distance[x][y] != -1 and grid[x][y] != 0:
                            # 가장 긴 경로를 찾아 시작과 끝의 합을 구한다
                            if distance[x][y] > max_length:
                                max_length = distance[x][y]
                                max_sum = grid[i][j] + grid[x][y]
                            elif distance[x][y] == max_length:
                                max_sum = max(max_sum, grid[i][j] + grid[x][y])
    
    return max_sum

# 입력 받기
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(find_max_password(n, m, grid))
