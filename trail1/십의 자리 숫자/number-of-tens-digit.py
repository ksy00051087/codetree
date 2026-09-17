arr1 = list(map(int, input().split()))
arr = []
for el in arr1:
    if el == 0:
        break
    arr.append(el // 10)
c_arr = [0] * 9
for i in arr:
    if i != 0:
        c_arr[i - 1] += 1
for j in range(1, 10):
    print(f'{j} - {c_arr[j - 1]}')
    
