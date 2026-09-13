N = int(input())
cnt = 0
x = 'A'

for i in range(N):
    for j in range(i):
        print(" ", end = " ")

    for j in range(N - i):
        print(chr(ord(x) + cnt), end = ' ')
        if cnt >= 25:
            cnt = 0
        else:
            cnt += 1
    print()