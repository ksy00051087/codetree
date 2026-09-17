c_arr = [0] * 4
cnt = 0
for _ in range(3):
    arr = input().split()
    tem = int(arr[1])
    if arr[0] == 'Y' and tem >= 37:
        c_arr[0] += 1
        cnt += 1
    elif arr[0] == 'Y' and tem < 37:
        c_arr[2] += 1
    elif arr[0] == 'N' and tem >= 37:
        c_arr[1] += 1
    elif arr[0] == 'N' and tem < 37:
        c_arr[3] += 1
if cnt >= 2:
    c_arr.append("E")
for i in c_arr:
    print(i, end = ' ')
    