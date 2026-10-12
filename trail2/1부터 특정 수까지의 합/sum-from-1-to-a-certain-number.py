n = int(input())

def krr(n):
    sum_val = 0  
    for i in range(1, n + 1):
        sum_val += i
    ans = sum_val // 10
    print(ans)

krr(n)

