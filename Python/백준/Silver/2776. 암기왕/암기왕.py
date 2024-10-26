T = int(input())

for _ in range(T):
    # 수첩 1
    N = int(input())
    notebook1 = set(map(int, input().split()))
    
    # 수첩 2
    M = int(input())
    notebook2 = list(map(int, input().split()))
    
    result = []
    for num in notebook2:
        if num in notebook1:
            result.append('1')
        else:
            result.append('0')
    
    print('\n'.join(result))
