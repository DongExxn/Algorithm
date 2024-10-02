def solution(number, limit, power):
    arr = [0] * (number + 1)

    # 약수의 개수를 계산 (루트 값을 활용하여 효율적으로 구함)
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            arr[j] += 1
    
    for i in range(len(arr)):
        if arr[i] > limit:
            arr[i] = power
            
    return sum(arr)