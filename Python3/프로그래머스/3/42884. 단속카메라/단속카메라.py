def solution(routes):
    # 차량의 경로를 시작 지점을 기준으로 정렬
    routes.sort(key=lambda x: x[0])
    
    # 첫 번째 차량의 종료 지점에 카메라를 설치
    camera_position = routes[0][1]
    cameras = 1
    
    for route in routes[1:]:
        # 현재 카메라가 다음 차량의 시작 지점을 커버할 수 없는 경우
        if camera_position < route[0]:
            # 새로운 카메라를 이 차량의 종료 지점에 설치
            cameras += 1
            camera_position = route[1]
        else:
            # 현재 카메라가 다음 차량의 종료 지점까지 커버할 수 있도록 위치 조정
            camera_position = min(camera_position, route[1])
    
    return cameras
