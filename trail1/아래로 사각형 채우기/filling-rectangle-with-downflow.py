n = int(input())
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]


for i in range(n):
    num = i + 1
    print(i + 1, end = ' ')
    for j in range(n):
        if j >= 1:
            arr[i][j] = num
            num += n 
            print(num, end = ' ')
    print()
