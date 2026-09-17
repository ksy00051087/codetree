n = int(input())
arr = list(map(int, input().split()))
cnt = 0
min_val = arr[0]
for i in arr:
    if i < min_val:
        min_val = i
for j in arr:
    if j == min_val:
        cnt += 1
print(min_val, cnt, end = ' ')