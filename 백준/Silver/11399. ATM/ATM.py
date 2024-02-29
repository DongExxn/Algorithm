n = int(input())

stack = []

stack = list(map(int, input().split()))

stack.sort()

answer = 0

for i in range(1, n+1):
    answer += sum(stack[0:i])

print(answer)


