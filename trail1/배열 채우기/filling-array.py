arr = list(map(int, input().split()))
arr1 = []
for i in arr:
    if i == 0 or len(arr1) == 10:
        break
    arr1.append(i)
rev_arr = arr1[::-1]

for i in rev_arr:
    print(i, end = ' ')