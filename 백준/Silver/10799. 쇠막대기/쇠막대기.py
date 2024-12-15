def count_pieces(s):
    stack = []
    pieces = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')  # 새로운 쇠막대기 시작
        else:
            stack.pop()  # 쇠막대기 끝
            if s[i-1] == '(':  # 바로 앞이 '('이면 레이저
                pieces += len(stack)  # 스택에 있는 쇠막대기만큼 잘린 조각이 추가됨
            else:  # 일반적인 닫는 괄호는 하나의 쇠막대기를 종료
                pieces += 1
    return pieces

# 입력 받기
s = input().strip()

# 결과 출력
print(count_pieces(s))
