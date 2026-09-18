N = int(input())
arr = list(map(int, input().split()))
arr1 = []
for i in arr:
    for j in arr:
        if i > j:
            arr1.append(i - j)
        elif j > i:
            arr1.append(j - i)
print(min(arr1))
        
