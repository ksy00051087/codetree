arr = list(map(int, input().split()))
arr1 = []
cnt = 0
for i in arr:
    if i == 0:
        break
    if i % 2 == 0:
        arr1.append(i)
        cnt += 1
sum_val = sum(arr1)
print(f'{cnt} {sum_val}')