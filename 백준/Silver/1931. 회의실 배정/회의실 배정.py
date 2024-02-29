num = int(input())

list = []

for i in range(num):
    start, end = map(int, input().split())
    list.append((start, end))

list.sort(key=lambda x: (x[1], x[0]))

end = list[0][1]
count = 1
for i in range(1, num):
    if end <= list[i][0]:
        end = list[i][1] 
        count += 1

print(count)


