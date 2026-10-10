N, M = map(int, input().split())

def kkr(N, M):
    num = 0
    for i in range(1, min(N, M) + 1):
        if N % i == 0 and M % i == 0:
            num = i
    print(num)

kkr(N, M)







