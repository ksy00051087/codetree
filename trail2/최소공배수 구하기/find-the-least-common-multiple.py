n, m = map(int, input().split())

def min_num(n, m):
    num = m
    while num % n != 0 or num % m != 0:
        num += 1
    return num

print(min_num(n, m))



