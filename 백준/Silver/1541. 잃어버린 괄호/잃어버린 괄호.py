list = input().split('-')

answer = []

for i in list:
    sum = 0
    temp = i.split('+')
    for j in temp:
        j = int(j)
        sum += j
    answer.append(sum)

result = answer[0]

for i in range(1, len(answer)):
    result -= answer[i]

print(result)
    