def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers)):
        # 스택이 비어있지 않고, 현재 수(numbers[i])가 스택의 마지막 인덱스의 수보다 큰 경우
        while stack and numbers[stack[-1]] < numbers[i]:
            index = stack.pop()
            answer[index] = numbers[i]
        stack.append(i)
    
    return answer