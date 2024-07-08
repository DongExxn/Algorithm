def solution(n, computers):
    count = 0
    
    def dfs(node):
        computers[node][node] = 0 # 자기 자신은 0으로 할당, False 형태
        
        for neibor in range(n):
            if computers[neibor][neibor] and computers[node][neibor]:
                dfs(neibor) #재귀호출
    
    for start in range(n):
        if computers[start][start]:
            dfs(start)
            count += 1
        
    return count