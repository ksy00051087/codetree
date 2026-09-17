arr = list(map(int, input().split()))
c_arr = [0] * 6
for i in arr:
    c_arr[i - 1] += 1
for tc in range(6):
    print(f'{tc + 1} - {c_arr[tc]}')