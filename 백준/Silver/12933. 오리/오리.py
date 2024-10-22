# 오리의 울음소리에서 최소 오리 수를 구하는 프로그램

def count_ducks():
    # 입력값 받기
    quack_sound = input().strip()

    # "quack"의 각 문자의 인덱스를 미리 준비
    quack = "quack"
    
    # 각 문자가 quack의 몇 번째 문자인지를 저장하는 배열
    step = {'q': 0, 'u': 1, 'a': 2, 'c': 3, 'k': 4}
    
    # 울음 소리의 상태를 추적하는 배열
    counts = [0] * 5  # quack의 각 단계에 있는 오리의 수
    ducks = 0  # 현재 울고 있는 오리의 수
    max_ducks = 0  # 동시에 울었던 오리의 최대 수
    
    for ch in quack_sound:
        if ch not in step:
            print(-1)  # quack에 없는 문자가 들어올 경우 잘못된 울음
            return
        
        idx = step[ch]
        
        if idx == 0:  # 'q'가 나왔을 때
            counts[0] += 1
            ducks += 1
            max_ducks = max(max_ducks, ducks)
        else:
            if counts[idx - 1] > 0:  # 이전 단계의 문자가 있는지 확인
                counts[idx - 1] -= 1
                counts[idx] += 1
                if idx == 4:  # 'k'일 때, 하나의 울음이 끝났으므로 ducks 감소
                    ducks -= 1
            else:
                print(-1)  # 순서가 잘못됨
                return
        
    if ducks != 0:  # 아직 울음이 끝나지 않은 오리가 있으면
        print(-1)
    else:
        print(max_ducks)

# 함수 실행
count_ducks()
