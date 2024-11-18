# 토너먼트

def find_round(N, a, b):
    round_num = 0

    # 두사람 번호가 같아질 때까지 반복
    while a != b:
        # 다음 라운드 번호 계산
        a = (a + 1) // 2
        b = (b + 1) // 2
        round_num += 1

    return round_num

N, a, b = map(int, input().split())
print(find_round(N, a, b))
