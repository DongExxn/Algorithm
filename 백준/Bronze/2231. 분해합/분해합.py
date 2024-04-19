n = int(input())

for i in range(1, n+1):
    m, tmp = i, i
    while tmp != 0:
        m += (tmp%10)
        tmp //= 10
        
    if m == n:
        print(i)
        break
    if i == n:
        print(0)
