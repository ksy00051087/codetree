N = int(input())
cnt = 0
arr = [i * N for i in range(1, 100)]
for j in arr:
    if cnt == 2:
        break
    if j % 5 == 0:
        cnt += 1
    print(j, end = ' ')


