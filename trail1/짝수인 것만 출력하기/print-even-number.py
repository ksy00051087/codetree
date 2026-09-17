N = int(input())
arr = list(map(int, input().split()))
arr1 = []
for i in arr:
    if i % 2 == 0:
        arr1.append(i)
for j in arr1:
    print(j, end = ' ')