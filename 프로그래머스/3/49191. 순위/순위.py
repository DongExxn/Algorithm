from collections import deque

def bfs(graph, start, n):
    q = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    count = 0
    
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
                count += 1
    
    return count

def solution(n, results):
    answer = 0
    
    win_graph = [[] for _ in range(n + 1)]
    lose_graph = [[] for _ in range(n + 1)]
    
    for a, b in results:
        win_graph[a].append(b)
        lose_graph[b].append(a)
    
    for i in range(1, n + 1):
        if bfs(win_graph, i, n) + bfs(lose_graph, i, n) == n - 1:
            answer += 1
    
    return answer
