from collections import deque

def solution(tickets):
    answer = []
    visit = [False for _ in range(len(tickets))] # 방문 초기화

    def DFS(start, path):
        if len(path) == len(tickets)+1:
            answer.append(path)
            return

        for idx, target in enumerate(tickets):
            if start == target[0] and visit[idx] == False:
                visit[idx] = True
                DFS(target[1], path+[target[1]])
                visit[idx] = False #백트래킹
    
    
    DFS("ICN", ["ICN"])
    answer.sort()
    return answer[0]
            
            