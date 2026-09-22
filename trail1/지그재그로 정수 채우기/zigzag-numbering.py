N, M = map(int, input().split())

for i in range(N):
    for j in range(M):
        if j % 2 == 0:
            # 짝수 열 (0, 2...): 위에서 아래로 정상 증가
            val = (j * N) + i
        else:
            # 홀수 열 (1, 3...): 밑에서 위로 역순 감소
            val = (j * N - 1) + (N - i)
            
        print(val, end=' ')
    print()