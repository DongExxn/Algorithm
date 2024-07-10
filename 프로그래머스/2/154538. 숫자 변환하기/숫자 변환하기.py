from collections import deque
    

def solution(x, y, n):
    answer = 0
    
    visited = [False] * (y + 1)
    
    # BFS를 위한 큐 초기화
    q = deque([(x, 0)])  # (현재 값, 현재까지의 연산 횟수)

    
    while q:
        current, count = q.popleft()
        
        # 현재 값이 y와 같다면 현재까지의 연산 횟수를 반환
        if current == y:
            return count
        
         # 다음 가능한 값들 계산
        next_values = [current + n, current * 2, current * 3]
        
        for next_val in next_values:
            # 다음 값이 y 이하이고 아직 방문하지 않은 값이라면 큐에 추가
            if next_val <= y and not visited[next_val]:
                visited[next_val] = True
                q.append((next_val, count + 1))
    
    # 큐가 빌 때까지 y를 찾지 못했다면 변환 불가
    return -1