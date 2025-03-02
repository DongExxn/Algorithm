#10진수를 3진수로 변환
def tentothree(n):
    temp = ''
    while n != 0:
        temp += str(n % 3)
        n = n // 3
    return temp

#3진수를 10진수로 변환
def threetoten(n):
    n = str(n)
    result = 0
    for i in range(len(n)):
        result += (3 ** i) * (int(n[-1-i]))
    return result 

def solution(n):    
    answer = int(tentothree(n))
    answer = threetoten(answer)
    return answer