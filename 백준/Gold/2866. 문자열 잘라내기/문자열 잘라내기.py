# 입력 처리
import sys
input = sys.stdin.read
data = input().split()

R, C = map(int, data[:2])
table = data[2:]

# 중복 검사 함수
def is_unique(row_count):
    seen = set()
    for col in range(C):
        # 각 열을 행 row_count부터 끝까지 문자열로 만듦
        column_string = ''.join(table[row][col] for row in range(row_count, R))
        if column_string in seen:
            return False
        seen.add(column_string)
    return True

# 이진 탐색
left, right = 0, R - 1
answer = 0

while left <= right:
    mid = (left + right) // 2
    if is_unique(mid):
        answer = mid
        left = mid + 1  # 더 많은 행을 제거할 수 있는지 확인
    else:
        right = mid - 1  # 중복 발생 시 행을 줄임

# 결과 출력
print(answer)
