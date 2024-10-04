num = int(input())
n = []
for i in range(num):
    n.append(list(map(int,input().split())))


first = n[0][0]

for i in range(1, num):
    for j in range(i+1):
        if j == 0:
            n[i][j] += n[i-1][0]
        elif j == i:
            n[i][j] += n[i-1][i-1]
        else:
            n[i][j] += max(n[i-1][j-1], n[i-1][j])

print(max(n[-1]))