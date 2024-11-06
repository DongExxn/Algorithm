import sys
input = sys.stdin.readline

# 입력 받기
N, D = map(int, input().split())
shortcuts = []
for _ in range(N):
    start, end, length = map(int, input().split())
    if end <= D and end > start:  # 고속도로 범위 내에 있는 유효한 지름길만 사용
        shortcuts.append((start, end, length))

# 초기 거리 배열 설정 (일반 도로 사용 시 거리)
distance = list(range(D + 1))

# 0부터 D까지 최소 거리 계산
for i in range(D + 1):
    # 바로 다음 지점으로 가는 경우(1km 이동)
    if i + 1 <= D:
        distance[i + 1] = min(distance[i + 1], distance[i] + 1)
    
    # 지름길 사용하는 경우 최소 거리 갱신
    for start, end, length in shortcuts:
        if i == start:
            distance[end] = min(distance[end], distance[i] + length)

# 출력: D 지점까지의 최소 거리
print(distance[D])
