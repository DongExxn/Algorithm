n = int(input())
arr = list(map(int, input().split()))
x = int(input())

count = 0
num_dict = {}

for number in arr:
    # 필요한 수 계산
    complement = x - number
    
    # complement가 이미 딕셔너리에 있는 경우 그 수의 개수를 더함
    if complement in num_dict:
        count += num_dict[complement]
    
    # 현재 수를 추가
    if number in num_dict:
        num_dict[number] += 1
    else:
        num_dict[number] = 1


print(count)
