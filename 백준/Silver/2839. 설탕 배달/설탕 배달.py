from collections import deque

# 입력 받기
n = int(input())

# BFS 탐색을 위한 큐 초기화
q = deque([(n, 0)])

# 방문한 상태를 기록하기 위한 리스트 초기화
visited = [False] * (n + 1)

while q:
    current_weight, count = q.popleft()
    
    # 만약 현재 무게가 0이면 정확하게 나눌 수 있는 경우이므로 봉지 개수 출력 후 종료
    if current_weight == 0:
        print(count)
        break
    
    # 현재 무게가 0보다 작으면 더 이상 탐색할 필요 없음
    if current_weight < 0:
        continue
    
    # 방문한 무게는 다시 방문하지 않도록 설정
    if not visited[current_weight]:
        visited[current_weight] = True
        
        # 5kg 봉지를 사용할 경우
        q.append((current_weight - 5, count + 1))
        # 3kg 봉지를 사용할 경우
        q.append((current_weight - 3, count + 1))
else:
    # 큐가 비워질 때까지도 0을 만들지 못한 경우 -1 출력
    print(-1)
