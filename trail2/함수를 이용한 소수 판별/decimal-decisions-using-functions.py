a, b = map(int, input().split())

def is_p(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def sum_p(a, b):
    sum_val = 0
    for j in range(a, b + 1):
        if is_p(j):
            sum_val += j
    return sum_val

print(sum_p(a, b))



