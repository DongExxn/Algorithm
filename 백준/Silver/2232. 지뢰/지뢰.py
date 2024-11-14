import sys

n = int(sys.stdin.readline().strip()) 
strengths = [int(sys.stdin.readline().strip()) for _ in range(n)] 

#터뜨려야 하는 지뢰
detonations = []

for i in range(n):
    #왼쪽
    if i > 0:
        left = strengths[i - 1]  #i가 0보다 클 때는 왼쪽 지뢰 강도
    else:
        left = 0  #첫 번째 지뢰일 때
    #오른쪽
    if i < n - 1:
        right = strengths[i + 1]  #i가 마지막 인덱스보다 작을 때는 오른쪽 지뢰 강도
    else:
        right = 0  #마지막 지뢰일 때

    #지뢰가 양쪽 지뢰보다 강하면 터뜨림
    if left <= strengths[i] >= right:
        detonations.append(i + 1) 

print('\n'.join(map(str, detonations)))
