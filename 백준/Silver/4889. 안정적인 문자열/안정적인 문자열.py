case_number = 1

while True:
    s = input().strip()
    if s.startswith('-'):
        break
    
    stack = []
    for char in s:
        if char == '{':
            stack.append(char)
        else:  # char == '}'
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(char)
    
    # 여는 괄호와 닫는 괄호의 개수
    open_count = stack.count('{')
    close_count = stack.count('}')
    
    # 최소 연산 수 계산
    result = (open_count + 1) // 2 + (close_count + 1) // 2
    print(f"{case_number}. {result}")
    
    case_number += 1
