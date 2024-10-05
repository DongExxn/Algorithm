import itertools

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = -1

    arr = list(itertools.combinations(nums, 3))
    
    cnt = 0
    for i in arr:
        if isPrime(sum(i)):
            cnt += 1
    return cnt