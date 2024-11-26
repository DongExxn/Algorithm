import sys
from collections import deque

# 입력 받기
input = sys.stdin.read
data = input().splitlines()

# 초기 문자열을 리스트로 변환 (왼쪽 스택)
left_stack = deque(data[0])

# 오른쪽 스택
right_stack = deque()

# 명령어 개수
m = int(data[1])

# 명령어 처리
commands = data[2:]

for command in commands:
    if command[0] == 'L':  # 커서를 왼쪽으로 이동
        if left_stack:
            right_stack.appendleft(left_stack.pop())
    elif command[0] == 'D':  # 커서를 오른쪽으로 이동
        if right_stack:
            left_stack.append(right_stack.popleft())
    elif command[0] == 'B':  # 커서 왼쪽 문자 삭제
        if left_stack:
            left_stack.pop()
    elif command[0] == 'P':  # 커서 왼쪽에 문자 추가
        left_stack.append(command[2])

# 결과 출력
print(''.join(left_stack) + ''.join(right_stack))
