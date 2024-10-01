def solution(a, b, n):
    total_cola = 0
    
    while n >= a:
        # 콜라로 교환할 수 있는 병의 수
        new_cola = (n // a) * b
        
        # 교환 후 남은 병의 수
        remaining_bottles = n % a
        
        # 총 콜라 수에 이번에 얻은 콜라 병 수를 더함
        total_cola += new_cola
        
        # 남은 병 + 이번에 얻은 콜라 병의 빈 병이 다음 반복의 n이 됨
        n = new_cola + remaining_bottles
        
    return total_cola
