from collections import deque

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    count = 1
    
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
                count += 1
    
    return count

def solution(n, wires):
    answer = 101
    
    for i in range(len(wires)):
        graph = [[] for _ in range(n + 1)]
        
        # 전선을 하나 제거하고 그래프 생성
        for j, (a, b) in enumerate(wires):
            if i == j:
                continue
            graph[a].append(b)
            graph[b].append(a)
        
        # BFS를 사용하여 두 서브 트리의 크기를 계산
        visited = [False] * (n + 1)
        subtree_size = bfs(graph, 1, visited)  # 아무 노드에서나 시작
        
        # 두 서브 트리의 크기 차이를 계산하고 최소값 갱신
        diff = abs((n - subtree_size) - subtree_size)
        answer = min(answer, diff)
    
    return answer
