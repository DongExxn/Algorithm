# 입력 처리
N = int(input())  # 배열의 길이
A = list(map(int, input().split()))  # 배열 A
B = list(map(int, input().split()))  # 배열 B

# A를 오름차순으로 정렬
A.sort()

# B를 내림차순으로 정렬
B.sort(reverse=True)

# S 값 계산
S = 0
for i in range(N):
    S += A[i] * B[i]

# 결과 출력
print(S)