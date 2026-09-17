N = int(input())
arr = [1, N]
arr1 = []
for i in range(2,100):
    a = arr[i - 1] + arr[i - 2]
    arr.append(a)
for j in arr:
    print(j, end = ' ')
    if j > 100:
        break
