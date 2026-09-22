N, M = map(int, input().split())

for i in range(N):
    for j in range(M):
        if j % 2 == 0:
            val = (j * N) + i
        else:
            val = (j * N - 1) + (N - i)
            
        print(val, end=' ')
    print()