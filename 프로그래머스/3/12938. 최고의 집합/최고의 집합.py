def solution(n, s):
    if s < n:
        return [-1]
    
    # 최대한 균등하게 분배해야 곱이 최대가 된다는 원리
    answer = [s // n] * n
    
    # 뒤에서부터 (s % n)개를 +1
    for i in range(n - 1, n - 1 - (s % n), -1):
        answer[i] += 1

    return answer