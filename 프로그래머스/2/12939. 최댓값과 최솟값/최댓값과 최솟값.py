def solution(s):
    answer = ''
    s = list(map(int,s.split(' '))) #int형으로 바꾸고 list를 만들어줌
    s.sort() #정렬
    min = s.pop(0)
    max = s.pop()
    return str(min)+' '+str(max) #문자로 바꾼 뒤에 공백을 넣어 출력

