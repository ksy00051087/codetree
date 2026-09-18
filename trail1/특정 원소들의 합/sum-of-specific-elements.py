arr = [list(map(int, input().split())) for _ in range(4)]

arr1 = []
for i in range(4):
    for j in range(i + 1):
        a = arr[i][j]
        arr1.append(a)
sum_val = sum(arr1)
print(sum_val)