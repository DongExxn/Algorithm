#선분 위의 점
import sys

n, m = map(int, sys.stdin.readline().rstrip().split(' '))

arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))
arr.sort()

results = []

# 이분 탐색 함수
def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

for i in range(m):
    start, end = map(int, sys.stdin.readline().rstrip().split(' '))

    # 이분 탐색을 사용해 점의 개수 계산
    left_idx = lower_bound(arr, start)
    right_idx = upper_bound(arr, end)

    # 선분 내 점의 개수 계산
    count = right_idx - left_idx
    results.append(str(count))

print("\n".join(results))