def solution(n, arr1, arr2):
    graph1 = []
    graph2 = []
    answer = [[''] * n for _ in range(n)]
    result = []
    
    for i in arr1:
        graph1.append(format(i, f'0{n}b'))
    
    for i in arr2:
        graph2.append(format(i, f'0{n}b'))
    
    for i in range(n):
        for j in range(n):
            if graph1[i][j] == '0' and graph2[i][j] == '0':
                answer[i][j] += ' '
            else:
                answer[i][j] += '#'
    for i in answer:
        result.append(''.join(i))
    
    return result