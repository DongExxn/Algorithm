def solution(s, n):
    answer = []
    for i in s:
        if 'A' <= i <= 'Z':  # 대문자일 때
            new_char = chr((ord(i) - ord('A') + n) % 26 + ord('A'))
        elif 'a' <= i <= 'z':  # 소문자일 때
            new_char = chr((ord(i) - ord('a') + n) % 26 + ord('a'))
        else:
            new_char = i  # 알파벳이 아닌 문자는 그대로 유지
        
        answer.append(new_char)
    return ''.join(answer)