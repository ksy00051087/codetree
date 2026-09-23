n=int(input())
num=1
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for j in range(n-1,-1,-1):
    for i in range(n-1,-1,-1):
        if (n-1-j)%2==0:
            arr[i][j]=num
            num+=1
        else:
            arr[n-1-i][j]=num
            num+=1

for row in arr:
    for elem in row:
        print(elem,end=" ")
    print()
