arr1 = list(map(int, input().split()))
c_arr = [0] * 10

for el in arr1:
    if el < 1:
        break
    idx = el // 10 - 1
    if idx < 0:      
        continue
    c_arr[idx] += 1

for j in range(9, -1, -1):
    print(f'{(j + 1) * 10} - {c_arr[j]}')