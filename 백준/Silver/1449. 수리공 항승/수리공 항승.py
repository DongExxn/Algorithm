n, l = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))
arr.sort()

cnt = 0
index = 0
position = 0


while index  < n:
    cnt += 1  
        # 테이프가 덮을 수 있는 범위 계산
    position = arr[index] + l - 1
        # 테이프가 덮을 수 있는 범위 안에 있는 위치만큼 index 추가
    while index < n and arr[index] <= position:
        index += 1
    
print(cnt)  
