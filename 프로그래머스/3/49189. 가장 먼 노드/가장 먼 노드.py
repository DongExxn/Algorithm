from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    visited = [0] * (n+1)
    result = [0] * (n+1)
    
    q = deque()
    q.append(1)
    
    #bfs
    while q:
        x = q.popleft()
        visited[x] = True
        for nx in graph[x]:
            if visited[nx] == 0:
                result[nx] = result[x] + 1
                visited[nx] = True
                q.append(nx)
    
    return result.count(max(result))