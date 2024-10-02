n,k = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))

temp_sum = sum(arr[:k]) # 구간합
max_sum = temp_sum
count = 1

for i in range(1, n-k+1):
    # 구간합 구해놓고 맨앞,맨뒤 값 빼고 더해주는 방식
    temp_sum = temp_sum - arr[i-1] + arr[i+k-1]

    if temp_sum > max_sum:
        max_sum = temp_sum
        count = 1
    elif temp_sum == max_sum:
        count += 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)