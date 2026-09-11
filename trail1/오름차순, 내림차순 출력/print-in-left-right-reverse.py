N = int(input())

for i in range(N):
    for j in range(N):
        if i % 2 == 1:
            print(N - j, end = '')
        else:
            print(j + 1, end = '')
    print()