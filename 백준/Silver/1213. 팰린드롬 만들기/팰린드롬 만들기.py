from collections import Counter

name = input().strip()
char_count = Counter(name)

odd_count = 0
middle_char = ""
for char, count in char_count.items():
    if count % 2 == 1:
        odd_count += 1
        middle_char = char

if odd_count > 1:
    print("I'm Sorry Hansoo")
else:
    first_half = []
    for char in sorted(char_count.keys()):
        first_half.append(char * (char_count[char] // 2))
    
    first_half = ''.join(first_half)
    result = first_half + middle_char + first_half[::-1]
    print(result)
