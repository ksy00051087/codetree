N = int(input())
arr = list(map(int, input().split()))

arr1 = []
while True:
    a = arr.index(max(arr))
    arr1.append(a + 1)
    if a + 1 == 1:
        break
    arr = arr[:a:]

for i in arr1:
    print(i, end = ' ')