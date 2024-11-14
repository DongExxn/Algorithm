import sys

# 입력 받기
N = int(sys.stdin.readline().strip())  # 지뢰의 개수 입력
strengths = [int(sys.stdin.readline().strip()) for _ in range(N)]  # 지뢰의 충격 강도 입력

# 직접 터뜨려야 하는 지뢰를 저장할 리스트
detonations = []

# 각 지뢰에 대해 직접 터뜨려야 하는지 확인
for i in range(N):
    # 이전 지뢰와 비교 (첫 번째 지뢰는 앞에 없으므로 0으로 비교)
    left = strengths[i - 1] if i > 0 else 0
    # 다음 지뢰와 비교 (마지막 지뢰는 뒤에 없으므로 0으로 비교)
    right = strengths[i + 1] if i < N - 1 else 0

    # 해당 지뢰가 좌우 지뢰보다 강하다면 터뜨려야 하는 지뢰
    if left <= strengths[i] >= right:
        detonations.append(i + 1)  # 인덱스는 1-based이므로 i + 1을 추가

# 결과 출력
print('\n'.join(map(str, detonations)))
