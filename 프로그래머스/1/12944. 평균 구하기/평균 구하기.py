def solution(arr):
    length = len(arr)
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        
    answer = sum / length
    return answer