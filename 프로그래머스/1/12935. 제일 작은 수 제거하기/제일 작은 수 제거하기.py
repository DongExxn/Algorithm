def solution(arr):
    mini = float('inf')
    
    if len(arr) == 1:
        return [-1]
    else:
        for i in range(len(arr)):
            if mini >  arr[i]:
                mini = arr[i]
        arr.remove(mini)
        return arr
        