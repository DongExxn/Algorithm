from collections import deque

n = int(input())
jump = list(map(int, input().split()))
start = int(input()) - 1

visited = [False] * n
queue = deque([start])
visited[start] = True
count = 1

while queue:
    current = queue.popleft()
    for direction in [-1, 1]:
        next_pos = current + direction * jump[current]
        if 0 <= next_pos < n and not visited[next_pos]:
            visited[next_pos] = True
            queue.append(next_pos)
            count += 1

print(count)
