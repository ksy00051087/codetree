def ans(N):
    sum_val = 0
    for i in range(1, N + 1):
        sum_val += i
    print(sum_val // 10)

N = int(input())
ans(N)
