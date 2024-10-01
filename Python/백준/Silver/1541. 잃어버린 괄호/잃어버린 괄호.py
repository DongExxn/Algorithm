text = input()

arr = list(text.split("-"))

temp = []
for i in arr:
    temp.append(sum(list(map(int, i.split('+')))))
    
answer = temp[0]

for i in range(1, len(temp)):
    answer -= temp[i]      
    
print(answer)