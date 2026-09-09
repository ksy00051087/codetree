n, q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(q):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        print(arr[cmd[1]-1])
    elif cmd[0] == 2:
        try:
            print(arr.index(cmd[1]) + 1)
        except ValueError:
            print(0)
    else:
        print(*arr[cmd[1]-1:cmd[2]])