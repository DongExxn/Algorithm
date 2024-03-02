num = input()
sum = 0
list = []

if '0' not in num:
    print(-1)
else:
    for i in num:
        i = int(i)
        sum += i
        list.append(i)
    if sum % 3 != 0:
        print(-1)
    else:
        list.sort(reverse=True)
        print(''.join(map(str, list)))