n, k = map(int, input().split())

stack = []
result = 0

for i in range(n):
    stack.append(int(input()))


for i in range(len(stack)):
        if k >= stack[-i-1]:
            result += k // stack[-i-1]
            k = k % stack[-i-1]
print(result)