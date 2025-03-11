def solution(A, B):
    A.sort() 
    B.sort()  
    i, j = 0, 0  
    score = 0  

    while j < len(B):
        if B[j] > A[i]:  # B가 A를 이길 수 있는 경우
            score += 1
            i += 1  # A의 다음 선수로 이동
        j += 1  # B의 다음 선수로 이동

        if i >= len(A):  # 모든 A팀 선수가 경기했으면 종료
            break

    return score
