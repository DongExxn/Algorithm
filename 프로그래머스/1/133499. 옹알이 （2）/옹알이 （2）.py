import itertools

def solution(babbling):
    answer = 0
    speaks = ['aya', 'ye', 'woo', 'ma']
    
    for babble in babbling:
        for speak in speaks:
            if speak * 2 not in babble:
                babble = babble.replace(speak, ' ')
        if babble.isspace():
            answer += 1
            
    return answer