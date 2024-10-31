T = int(input())  # 테스트 케이스 개수 입력 받기

for i in range(1, T + 1):
    A, B = map(int, input().split())  # 각 테스트 케이스의 두 정수 입력 받기
    print(f"Case #{i}: {A + B}")