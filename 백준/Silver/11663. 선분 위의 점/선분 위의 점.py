import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dot = list(map(int, input().split()))
dot.sort()

def check(x, direction):
    left, right = 0, n-1

    while left <= right:
        mid = (left + right)//2

        if x < dot[mid]:
            right = mid - 1
        elif x > dot[mid]:
            left = mid + 1
        else:
            return mid

    if direction == 0:
        return left
    else:
        return right


for _ in range(m):
    a, b = map(int, input().split())
    l, r = check(a, 0), check(b, 1)
    print(r-l+1)