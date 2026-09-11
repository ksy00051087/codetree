a, b = map(int, input().split())
cnt = 0

for i in range(4):
    cnt += 2
    for j in range(b, a - 1, -1):
        print(f"{j} * {cnt} = {j * cnt}", end = ' ')
        if j > a:
            print("/", end = ' ')
    print()