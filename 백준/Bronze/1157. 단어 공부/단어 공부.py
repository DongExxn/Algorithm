text = input().upper()

# 문자를 카운트할 딕셔너리 생성
char_count = {}

# 문자 카운트
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# 가장 많이 나온 문자 찾기
max_count = max(char_count.values())
most_common_chars = [char for char, count in char_count.items() if count == max_count]

if len(most_common_chars) > 1:
    most_common_char = '?'
else:
    most_common_char = most_common_chars[0]

print(most_common_char)
