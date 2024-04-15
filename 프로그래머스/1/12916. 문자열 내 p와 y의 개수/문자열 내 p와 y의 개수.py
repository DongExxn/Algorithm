def solution(s):
    p_num = 0
    s_num = 0
    
    s = s.upper()
    for i in s:
        if i == 'P':
            p_num += 1
        elif i == 'Y':
            s_num += 1
    if p_num == s_num:
        return True
    else:
        return False

    return True