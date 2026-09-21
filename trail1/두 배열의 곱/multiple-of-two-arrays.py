N = 3
arr1 = [list(map(int, input().split())) for _ in range(N)]
s = input()
arr2 = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        print(f'{arr1[i][j] * arr2[i][j]}', end = ' ')
    print()