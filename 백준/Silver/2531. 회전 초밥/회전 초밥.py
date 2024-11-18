def max_sushi_variety(N, d, k, c, belt):
    # 초밥 종류 카운트를 위한 배열
    sushi_count = [0] * (d + 1)
    # 현재 윈도우에서의 초밥 종류 수
    current_variety = 0

    # 초기 윈도우 설정
    for i in range(k):
        if sushi_count[belt[i]] == 0:
            current_variety += 1
        sushi_count[belt[i]] += 1

    # 쿠폰 초밥 고려
    max_variety = current_variety + (1 if sushi_count[c] == 0 else 0)

    # 슬라이딩 윈도우 이동
    for i in range(N):
        # 윈도우의 시작과 끝 인덱스
        start = belt[i]
        end = belt[(i + k) % N]

        # 윈도우의 시작 초밥 제거
        sushi_count[start] -= 1
        if sushi_count[start] == 0:
            current_variety -= 1

        # 윈도우의 끝 초밥 추가
        if sushi_count[end] == 0:
            current_variety += 1
        sushi_count[end] += 1

        # 쿠폰 초밥 고려
        max_variety = max(max_variety, current_variety + (1 if sushi_count[c] == 0 else 0))

    return max_variety

# 입력 받기
N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]

# 결과 출력
print(max_sushi_variety(N, d, k, c, belt))
