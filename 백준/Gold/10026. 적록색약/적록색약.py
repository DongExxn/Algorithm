from collections import deque
import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, visited, graph, current_color):
    stack = deque()
    stack.append((x, y))
    visited[x][y] = True
    
    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] == current_color:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
graph_normal = [list(input()) for _ in range(n)]

# 적록색약 그래프
graph_colorblind = [row.copy() for row in graph_normal]
for i in range(n):
    for j in range(n):
        if graph_colorblind[i][j] == 'G':
            graph_colorblind[i][j] = 'R'

# 적록색약이 아닌 사람
visited_normal = [[False]*n for _ in range(n)]
count_normal = 0
for i in range(n):
    for j in range(n):
        if not visited_normal[i][j]:
            dfs(i, j, visited_normal, graph_normal, graph_normal[i][j])
            count_normal += 1 

# 적록색약인 사람
visited_colorblind = [[False]*n for _ in range(n)]
count_colorblind = 0
for i in range(n):
    for j in range(n):
        if not visited_colorblind[i][j]:
            dfs(i, j, visited_colorblind, graph_colorblind, graph_colorblind[i][j])
            count_colorblind += 1 

print(count_normal, count_colorblind)
