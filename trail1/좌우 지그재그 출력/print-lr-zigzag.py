N = int(input())
cnt = 0

for i in range(N):
    if i % 2 == 0:
        for j in range(N):
            cnt += 1
            print(cnt, end = ' ')
    else:
        cnt += N
        for j in range(N):
            print(cnt - j, end = ' ')
    print()

