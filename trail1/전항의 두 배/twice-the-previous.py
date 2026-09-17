
arr = list(map(int, input().split()))
for i in range(2, 10):
    a = arr[i - 1] + (2 * arr[i - 2])
    arr.append(a)
for j in arr:
    print(j, end = ' ')
