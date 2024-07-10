def solution(order):
    answer = 0
    stack = []
    idx = 0
    
    for i in range(1, len(order) + 1):
        if i == order[idx]:
            answer += 1
            idx += 1
            # 스택에서 가능한 상자를 모두 트럭에 싣기
            while stack and stack[-1] == order[idx]:
                stack.pop()
                answer += 1
                idx += 1
        else:
            stack.append(i)
    
    return answer