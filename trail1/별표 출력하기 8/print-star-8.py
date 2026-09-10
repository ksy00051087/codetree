N = int(input())

for i in range(N):
    if i % 2 != 0:
        for j in range(i + 1):
            print("*", end = " ")
        print()
    else:
        print("*")