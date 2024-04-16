def solution(board, moves):
    # [0,0,0,0,0]
    # [0,0,1,0,3]
    # [0,2,5,0,1]
    # [4,2,4,4,2]
    # [3,5,1,3,1]
    
    answer = 0
    
    stack = []
    
    for i in moves:
        for j in range(len(board)):
            # print(board[j][i-1])
            if board[j][i-1] != 0:
                stack.append(board[j][i-1])
                if len(stack)>1 and (stack[-1] == stack[-2]):
                    stack.pop()
                    stack.pop()
                    answer+=2
                board[j][i-1] = 0
                break
        
    return answer