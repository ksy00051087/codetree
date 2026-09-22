N, M = map(int,input().split())
num=1

arr = [
    [0 for _ in range(M)]
    for _ in range(N)
]

for z in range(N + M + 1):
    for i in range(N):
        for j in range(M):
            if i + j == z :
                arr[i][j]=num
                num+=1

for row in arr:
    for elem in row:
        print(elem,end=" ")
    print()
