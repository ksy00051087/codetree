N = int(input())

cnt = N
a = 0
for i in range(1, N + 1):
    cnt = cnt // i
    a += 1
    if cnt <= 1:
        break
print(a)


