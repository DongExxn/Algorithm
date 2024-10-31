# 입력 받기
import sys
input = sys.stdin.read
data = input().splitlines()

# 첫 번째 줄: 문제 수 N
N = int(data[0])

# 두 번째 줄: 각 난이도별로 풀어야 하는 문제 수
p = list(map(int, data[1].split()))

# 세 번째 줄부터 각 문제의 난이도와 풀이 시간
problems = []
for line in data[2:]:
    k, t = map(int, line.split())
    problems.append((k, t))

# 난이도별로 문제들을 저장할 리스트
levels = [[] for _ in range(5)]

# 각 문제를 난이도별로 분류
for k, t in problems:
    levels[k - 1].append(t)  # 난이도 1~5 -> 인덱스 0~4

# 난이도별로 필요한 문제 수만큼 최소 시간이 드는 순으로 풀기 위해 정렬
for i in range(5):
    levels[i].sort()

total_time = 0  # 총 걸리는 시간

# 난이도 1부터 5까지 순차적으로 문제 풀이
for i in range(5):
    required_problems = p[i]
    selected_problems = levels[i][:required_problems]  # 최소 시간의 문제 선택

    # 같은 난이도에서의 문제 시간 및 휴식 시간 계산
    for j, time in enumerate(selected_problems):
        total_time += time
        if j > 0:  # 동일 난이도에서 두 문제 사이 시간 차이 추가
            total_time += time - selected_problems[j - 1]

    # 난이도가 증가할 때마다 60분 휴식 추가
    if i < 4 and p[i + 1] > 0:  # 마지막 난이도에서는 추가 휴식 없음
        total_time += 60

# 결과 출력
print(total_time)
