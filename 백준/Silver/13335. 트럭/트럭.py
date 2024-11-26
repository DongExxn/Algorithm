import sys
from collections import deque

# 입력 받기
input = sys.stdin.read
lines = input().splitlines()

# 첫 줄: 트럭의 수, 다리의 길이, 다리의 최대 하중
n, w, L = map(int, lines[0].split())

# 두 번째 줄: 각 트럭의 무게
trucks = list(map(int, lines[1].split()))

# 다리 위에 있는 트럭을 관리할 큐 (현재 다리 상태)
bridge = deque([0] * w)

current_weight = 0  # 현재 다리 위의 총 무게
time = 0  # 경과 시간

for truck in trucks:
    while True:
        time += 1
        # 다리에서 가장 앞의 트럭을 내보냄
        current_weight -= bridge.popleft()

        # 트럭을 다리에 올릴 수 있는지 확인
        if current_weight + truck <= L:
            # 트럭을 다리에 올림
            bridge.append(truck)
            current_weight += truck
            break
        else:
            # 트럭을 올릴 수 없으면 빈 공간(0)을 추가
            bridge.append(0)

# 마지막 트럭이 다리를 완전히 건너기 위한 시간 추가
time += w

# 결과 출력
print(time)
