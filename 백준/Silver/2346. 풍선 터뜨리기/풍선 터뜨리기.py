from collections import deque

num = int(input())

arr = list(map(int, input().split(' ')))
balloons = list(range(1, num + 1))
idx = 0
result = []

while balloons:
    result.append(balloons.pop(idx))  # 현재 풍선 터뜨리기
    if not balloons:  # 더 이상 터뜨릴 풍선이 없으면 끝
        break
    move = arr[result[-1] - 1]  # 방금 터뜨린 풍선의 이동값 가져오기

    # move 만큼 이동하는데, 양수면 오른쪽, 음수면 왼쪽으로 이동
    if move > 0:
        idx = (idx + (move - 1)) % len(balloons)  # 양수면 오른쪽으로 이동, 터진 풍선 하나 건너뜀
    else:
        idx = (idx + move) % len(balloons)  # 음수면 왼쪽으로 이동

print(' '.join(map(str, result)))