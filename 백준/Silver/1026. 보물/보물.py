num = int(input())

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

list1.sort()
list2.sort(reverse=True)

result = 0

for i in range(num):
    result += list1[i] * list2[i]

print(result)