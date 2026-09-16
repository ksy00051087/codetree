arr = list(map(int, input().split()))
arr1 = sum(arr[::2])
arr2 = sum(arr[1::2])
if arr1 > arr2:
    print(arr1 - arr2)
elif arr2 > arr1:
    print(arr2 - arr1)
else:
    None