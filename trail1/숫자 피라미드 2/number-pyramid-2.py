N = int(input())
cnt = 0

for i in range(N):
    for j in range(i + 1):
        cnt += 1
        print(cnt, end = ' ')
    print()