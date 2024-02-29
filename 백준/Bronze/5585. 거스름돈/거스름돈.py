num = int(input())

list = [500, 100, 50, 10, 5, 1]

new_num = 1000 - num
count = 0

for i in range(len(list)): 
    if new_num >= list[i]:
        count += new_num // list[i]
        new_num = new_num % list[i]

print(count)
