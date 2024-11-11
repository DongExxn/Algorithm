from collections import deque

# 입력 받기
n = int(input())  # 동기의 수
m = int(input())  # 친구 관계의 수

# 그래프 초기화 (인접 리스트)
graph = [[] for _ in range(n + 1)]

# 친구 관계 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# BFS 탐색을 위한 초기 설정
visited = [False] * (n + 1)
queue = deque([(1, 0)])  # (현재 노드, 현재 깊이)
visited[1] = True
invited_count = 0

# BFS 탐색
while queue:
    current, depth = queue.popleft()
    
    # 깊이가 2를 넘으면 더 이상 탐색하지 않음
    if depth >= 2:
        continue
    
    # 친구 탐색
    for friend in graph[current]:
        if not visited[friend]:
            queue.append((friend, depth + 1))
            visited[friend] = True
            invited_count += 1

# 결과 출력
print(invited_count)
