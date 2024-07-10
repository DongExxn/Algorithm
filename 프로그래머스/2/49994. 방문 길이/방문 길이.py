def solution(dirs):
    # 초기 위치 설정
    x, y = 0, 0
    
    # 방문한 경로 저장을 위한 집합 (set)
    visited = set()
    
    # 이동 명령어에 따른 이동 변화량
    dx = [0, 0, 1, -1]  # U, D, R, L 순서
    dy = [1, -1, 0, 0]  # U, D, R, L 순서
    
    # 처음 걸어본 길의 길이를 저장할 변수
    length = 0
    
    # 명령어 하나씩 처리
    for d in dirs:
        # 현재 위치
        cur_x, cur_y = x, y
        
        # 이동할 새로운 위치 계산
        direction_index = {'U': 0, 'D': 1, 'R': 2, 'L': 3}
        idx = direction_index[d]
        nx, ny = cur_x + dx[idx], cur_y + dy[idx]
        
        # 좌표평면 경계 안에 있을 때만 이동
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            # 현재 위치와 새로운 위치를 통해 경로 설정
            path = (min((cur_x, cur_y), (nx, ny)), max((cur_x, cur_y), (nx, ny)))
            
            # 해당 경로를 처음 방문한 경우
            if path not in visited:
                visited.add(path)
                length += 1
            
            # 새로운 위치로 이동
            x, y = nx, ny
    
    return length
