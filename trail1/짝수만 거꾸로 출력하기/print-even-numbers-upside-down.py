N = int(input())
arr = list(map(int, input().split()))
arr1 = arr[::-1]
for i in arr1:
    if i % 2 == 0:
        print(i, end = ' ')