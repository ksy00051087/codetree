N = int(input())

for i in range(N):
    for j in range(N):
        if j % 2 == 1:
            print(N - i, end = '')
        else:
            print(i + 1, end = '')
    print()

