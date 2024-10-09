def check_count(x, y, n):
    global white, blue

    initial_color = arr[x][y]
    is_check = True


    for i in range(x,x+n):
        for j in range(y,y+n):
            if arr[i][j] != initial_color:
                is_check = False
                break
        if not is_check:
            break
    
    if is_check:
        if initial_color == 0:
            white += 1
        else:
            blue += 1
    else:
        half = n // 2
        check_count(x,y,half)
        check_count(x, y+half, half)
        check_count(x+half, y, half)
        check_count(x+half, y+half, half)
    

row = int(input())
col = row

white = 0
blue = 0

arr = []

# 2차원 배열 생성
for i in range(row):
    arr.append(list(map(int, input().split(' '))))

check_count(0, 0, row)

print(white)
print(blue)