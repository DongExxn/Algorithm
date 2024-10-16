num = int(input())

sum = 1
for i in range(1, num+1):
    sum *= i

sum = str(sum)

answer = sum[0]

for i in range(len(sum)-1, -1, -1):
    if int(sum[i]) != 0:
        print(int(sum[i]))
        break

