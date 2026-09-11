N = int(input())

for i in range(N):
    for j in range(i + 1):
        print(N - i + j, end=" ")
    print()