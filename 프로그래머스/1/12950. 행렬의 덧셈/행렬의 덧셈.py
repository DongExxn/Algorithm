def solution(arr1, arr2):
    answer = []
    
    stack = []
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            stack.append(arr1[i][j] + arr2[i][j])

        answer.append(stack)
        stack = []
    return answer