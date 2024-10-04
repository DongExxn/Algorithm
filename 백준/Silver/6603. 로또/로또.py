import itertools

while True:
    num = list(map(int, input().split(' ')))

    if num[0] == 0:  # 첫 번째 값이 0이면 종료
        break
    
    num = num[::-1]
    num.pop()
    num.sort()
    nCr = list(itertools.combinations(num, 6))
    
    for i in nCr:
        print(' '.join(map(str, i)))
    print()
