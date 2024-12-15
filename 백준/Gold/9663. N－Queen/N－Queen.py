# 입력 처리
import sys
input = sys.stdin.read
N = int(input().strip())

# 결과 변수
result = 0

# 상태 배열 초기화
cols = [False] * N  # 열 상태
diagonals1 = [False] * (2 * N - 1)  # ↘ 대각선 상태
diagonals2 = [False] * (2 * N - 1)  # ↙ 대각선 상태

# 백트래킹 함수
def solve(row):
    global result
    if row == N:  # 모든 행에 배치 완료
        result += 1
        return

    for col in range(N):  # 열 순회
        if not cols[col] and not diagonals1[row - col + N - 1] and not diagonals2[row + col]:
            # 현재 위치에 퀸 배치
            cols[col] = diagonals1[row - col + N - 1] = diagonals2[row + col] = True
            solve(row + 1)  # 다음 행으로 이동
            # 퀸 제거 (백트래킹)
            cols[col] = diagonals1[row - col + N - 1] = diagonals2[row + col] = False

# 함수 호출
solve(0)
print(result)
