def solution(array, commands):
    answer = []
    
    copy_temp = []
    
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        
        copy_temp = array[i-1:j]
        copy_temp.sort()
        answer.append(copy_temp[k-1])
    return answer