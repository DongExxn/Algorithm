# 단축키 지정

n = int(input())
options = [input() for _ in range(n)]

# 이미 사용된 단축키
used_shortcuts = set()

for option in options:
    words = option.split() 
    found = False  # 단축키가 지정되었는지 여부 확인 변수
    
    # 각 단어 첫 글자 확인
    for i, word in enumerate(words):
        if word[0].lower() not in used_shortcuts:
            used_shortcuts.add(word[0].lower())
            words[i] = f"[{word[0]}]{word[1:]}"  # 단축키 지정해주기
            found = True
            break
    
    # 모든 글자에서 단축키 찾기
    if not found:
        for i, word in enumerate(words):
            for j, char in enumerate(word):
                if char.lower() not in used_shortcuts:
                    used_shortcuts.add(char.lower())
                    words[i] = f"{word[:j]}[{char}]{word[j+1:]}"  # 단축키 지정해주기
                    found = True
                    break
            if found:
                break
    
    print(" ".join(words))
