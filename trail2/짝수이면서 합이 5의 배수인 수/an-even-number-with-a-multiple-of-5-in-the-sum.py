N = int(input())
def ans(N):
    a = N // 10
    b = a * 10
    c = N - b
    d = a + c
    if N % 2 == 0 and d % 5 == 0:
        print("Yes")
    else:
        print("No")
ans(N)