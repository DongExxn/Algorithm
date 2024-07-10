from itertools import permutations

n, m = map(int, input().split(' '))

# 1부터 n까지의 숫자로 이루어진 리스트 생성
numbers = []
for i in range(1, n+1):
    numbers.append(i)

# permutations를 사용하여 순열 생성
perms = list(permutations(numbers, m))

# 순열 리스트를 출력
for perm in perms:
    print(' '.join(map(str, perm)))
