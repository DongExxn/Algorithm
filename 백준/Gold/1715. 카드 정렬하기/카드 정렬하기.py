import heapq

num = int(input())

list = []

for i in range(num):
    heapq.heappush(list, int(input()))

# list.sort(reverse=True)

result = 0

while len(list) > 1:
    a = heapq.heappop(list)
    b = heapq.heappop(list)

    heapq.heappush(list, (a + b))
    result += (a + b)

print(result)



