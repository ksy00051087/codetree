N = int(input())
cnt = 0
x = 'A'
for i in range(N):
    for j in range(N):
        print(chr(ord(x) + cnt), end = "")
        cnt += 1
    print()