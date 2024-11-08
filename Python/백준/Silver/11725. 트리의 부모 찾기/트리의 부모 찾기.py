# 트리의 부모 찾기
import sys
 
N = int(sys.stdin.readline())
 
graph = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
 
visited = [0]*(N+1) 
 
def dfs(graph,node):
 
    stack = [node]
    while stack:
        top = stack.pop()
        for adj in graph[top]:
            if visited[adj] == 0: 
                visited[adj] = top
                stack.append(adj)
    
    return visited
 
dfs(graph, 1)
 
for x in range(2, N+1):
    print(visited[x]) 