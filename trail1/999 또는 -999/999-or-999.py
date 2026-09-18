arr = list(map(int, input().split()))
max_val = arr[0]
min_val = arr[0]
for i in arr:
    if i == -999 or i == 999:
        break
    if i > max_val:
        max_val = i

for j in arr:
    if j == -999 or j == 999:
        break
    if j < min_val:
        min_val = j
print(f'{max_val} {min_val}')
        